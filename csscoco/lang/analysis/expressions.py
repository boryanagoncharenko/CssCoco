import re

import csscoco
from csscoco.lang.ast import ast as ast
import csscoco.lang.analysis.values as values
import csscoco.lang.visitor_decorator as vis


class EvaluationContext(object):
    def __init__(self, pattern_matcher):
        self.pattern_matcher = pattern_matcher

    def get_node_by_id(self, identifier):
        raise NotImplementedError()

    def get_node_by_desc(self, desc):
        raise NotImplementedError()


class NodeConstraintContext(EvaluationContext):
    def __init__(self, pattern_matcher, node):
        super(NodeConstraintContext, self).__init__(pattern_matcher)
        assert node
        self._node = node

    def get_node_by_id(self, identifier):
        return self._node

    def get_node_by_desc(self, desc):
        return self._node


class ConventionConstraintContext(EvaluationContext):
    def __init__(self, pattern_matcher, id_to_node_table):
        super(ConventionConstraintContext, self).__init__(pattern_matcher)
        self._id_node_table = id_to_node_table

    def get_node_by_id(self, identifier):
        for desc in self._id_node_table:
            if desc.has_identifier() and desc.identifier == identifier:
                return self._id_node_table[desc]
        raise ValueError('Usage of unknown identifier: ' + identifier)

    def get_node_by_desc(self, desc):
        return self._id_node_table[desc]


class ExprEvaluator(object):
    def __init__(self, context):
        self._context = context

    @staticmethod
    def evaluate(expr, context):
        evaluator = ExprEvaluator(context)
        return evaluator.visit(expr)

    @vis.visitor(ast.NotExpr)
    def visit(self, not_expr):
        operand = self.visit(not_expr.operand)
        return operand.not_()

    @vis.visitor(ast.UnaryMinusExpr)
    def visit(self, unary_minus_expr):
        operand = self.visit(unary_minus_expr.operand)
        return operand.unary_minus()

    @vis.visitor(ast.OrExpr)
    def visit(self, or_expr):
        left = self.visit(or_expr.left)
        if not left.is_false():
            return values.Boolean.TRUE
        right = self.visit(or_expr.right)
        return left.or_(right)

    @vis.visitor(ast.AndExpr)
    def visit(self, and_expr):
        left = self.visit(and_expr.left)
        if left.is_false():
            return values.Boolean.FALSE
        right = self.visit(and_expr.right)
        return left.and_(right)

    @vis.visitor(ast.EqualExpr)
    def visit(self, equals_expr):
        left = self.visit(equals_expr.left)
        right = self.visit(equals_expr.right)
        return left.equals(right)

    @vis.visitor(ast.NotEqualExpr)
    def visit(self, not_equals_expr):
        left = self.visit(not_equals_expr.left)
        right = self.visit(not_equals_expr.right)
        return left.not_equals(right)

    @vis.visitor(ast.GreaterThanExpr)
    def visit(self, greater_than_expr):
        left = self.visit(greater_than_expr.left)
        right = self.visit(greater_than_expr.right)
        return left.greater_than(right)

    @vis.visitor(ast.LessThanExpr)
    def visit(self, less_than_expr):
        left = self.visit(less_than_expr.left)
        right = self.visit(less_than_expr.right)
        return left.less_than(right)

    @vis.visitor(ast.DecimalExpr)
    def visit(self, decimal_expr):
        return values.Decimal(decimal_expr.value)

    @vis.visitor(ast.IntegerExpr)
    def visit(self, integer_expr):
        return values.Integer(integer_expr.value)

    @vis.visitor(ast.StringExpr)
    def visit(self, string_expr):
        return values.String(string_expr.value)

    @vis.visitor(ast.BooleanExpr)
    def visit(self, boolean_expr):
        return values.Boolean.build(boolean_expr.value)

    @vis.visitor(ast.ListExpr)
    def visit(self, list_expr):
        vs = []
        for v in list_expr.value:
            nv = self.visit(v)
            vs.append(nv)
        return values.List(vs)

    @vis.visitor(ast.NodeTypeExpr)
    def visit(self, node_type_expr):
        return values.NodeType(node_type_expr.value)

    @vis.visitor(ast.VariableExpr)
    def visit(self, variable_expr):
        return values.Node(self._context.get_node_by_id(variable_expr.name))

    @vis.visitor(ast.Node)
    def visit(self, expr):
        return expr

    @vis.visitor(ast.IsExpr)
    def visit(self, is_expr):
        node_expr = self.visit(is_expr.left)
        type_expr = self.visit(is_expr.right)
        return node_expr.is_(type_expr)

    @vis.visitor(ast.MatchExpr)
    def visit(self, match_expr):
        operand = self.visit(match_expr.left)
        if not operand.value:
            return values.Boolean.TRUE
        regex = self.visit(match_expr.right)
        pattern = re.compile(regex.value)
        result = pattern.findall(operand.value)
        return values.Boolean.build(result)

    @vis.visitor(ast.InExpr)
    def visit(self, in_expr):
        operand = self.visit(in_expr.left)
        list_ = self.visit(in_expr.right)
        return operand.in_(list_)

    @vis.visitor(ast.PropertyExpr)
    def visit(self, prop_expr):
        node = self.visit(prop_expr.operand)
        real_node = node.value
        return real_node.invoke_property(prop_expr.value)

    @vis.visitor(ast.MethodExpr)
    def visit(self, method_expr):
        node = self.visit(method_expr.operand)
        real_node = node.value
        argument = self.visit(method_expr.argument)
        return real_node.invoke_method(method_expr.value, argument.value)

    @vis.visitor(ast.ContainsExpr)
    def visit(self, contains_expr):
        node_value = self.visit(contains_expr.operand)
        for d in self._context.pattern_matcher.find_descendants_that_match(node_value.value, contains_expr.argument):
            return values.Boolean.TRUE
        return values.Boolean.FALSE

    @vis.visitor(ast.ContainsAllExpr)
    def visit(self, contains_all_expr):
        node_value = self.visit(contains_all_expr.operand)
        list_value = contains_all_expr.argument
        result = self._context.pattern_matcher.find_all(node_value.value, list_value.value)
        return values.Boolean.build(result)

    @vis.visitor(ast.CountExpr)
    def visit(self, count_expr):
        node_value = self.visit(count_expr.operand)
        count = 0
        for _ in self._context.pattern_matcher.find_descendants_that_match(node_value.value, count_expr.argument):
            count += 1
        return values.Integer(count)

    @vis.visitor(ast.NextSiblingExpr)
    def visit(self, next_sibling):
        node_value = self.visit(next_sibling.operand)
        node = self._context.pattern_matcher.find_next_sibling(node_value.value)
        if node:
            return values.Node(node)
        return values.Undefined.VALUE

    @vis.visitor(ast.PreviousSiblingExpr)
    def visit(self, prev_sibling):
        node_value = self.visit(prev_sibling.operand)
        node = self._context.pattern_matcher.find_previous_sibling(node_value.value)
        if node:
            return values.Node(node)
        return values.Undefined.VALUE

    @vis.visitor(ast.BeforeExpr)
    def visit(self, before):
        operand_node_value = self.visit(before.operand)
        _filter = self._context.pattern_matcher.filter
        matcher = csscoco.lang.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_before_node(before.argument, operand_node_value.value)
        return values.Boolean.build(match)

    @vis.visitor(ast.BetweenExpr)
    def visit(self, between):
        left_node_value = self.visit(between.operand)
        right_node_value = self.visit(between.second_operand)
        _filter = self._context.pattern_matcher.filter
        matcher = csscoco.lang.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_between_nodes(between.argument, left_node_value.value, right_node_value.value)
        return values.Boolean.build(match)

    @vis.visitor(ast.AfterExpr)
    def visit(self, after):
        operand_node_value = self.visit(after.operand)
        _filter = self._context.pattern_matcher.filter
        matcher = csscoco.lang.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_after_node(after.argument, operand_node_value.value)
        return values.Boolean.build(match)

