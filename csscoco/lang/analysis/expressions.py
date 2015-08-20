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
    def __init__(self, pattern_matcher, id_to_node_table, stylesheet):
        super(ConventionConstraintContext, self).__init__(pattern_matcher)
        self._id_node_table = id_to_node_table
        self._stylesheet = stylesheet

    def get_node_by_id(self, identifier):
        if identifier == 'stylesheet':
            if not self._stylesheet:
                raise ValueError('Stylesheet is not defined')
            return self._stylesheet
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
        return evaluator._visit(expr)

    @vis.visitor(ast.NotExpr)
    def _visit(self, not_expr):
        operand = self._visit(not_expr.operand)
        return operand.not_()

    @vis.visitor(ast.UnaryMinusExpr)
    def _visit(self, unary_minus_expr):
        operand = self._visit(unary_minus_expr.operand)
        return operand.unary_minus()

    @vis.visitor(ast.UnaryPlusExpr)
    def _visit(self, unary_plus_expr):
        operand = self._visit(unary_plus_expr.operand)
        return operand.unary_plus()

    @vis.visitor(ast.OrExpr)
    def _visit(self, or_expr):
        left = self._visit(or_expr.left)
        if not left.is_false():
            return values.Boolean.TRUE
        return self._visit(or_expr.right)

    @vis.visitor(ast.AndExpr)
    def _visit(self, and_expr):
        left = self._visit(and_expr.left)
        if left.is_false():
            return values.Boolean.FALSE
        return self._visit(and_expr.right)

    @vis.visitor(ast.EqualExpr)
    def _visit(self, equals_expr):
        left = self._visit(equals_expr.left)
        right = self._visit(equals_expr.right)
        return left.equals(right)

    @vis.visitor(ast.NotEqualExpr)
    def _visit(self, not_equals_expr):
        left = self._visit(not_equals_expr.left)
        right = self._visit(not_equals_expr.right)
        return left.not_equals(right)

    @vis.visitor(ast.GreaterThanExpr)
    def _visit(self, greater_than_expr):
        left = self._visit(greater_than_expr.left)
        right = self._visit(greater_than_expr.right)
        return left.greater_than(right)

    @vis.visitor(ast.GreaterThanOrEqualExpr)
    def _visit(self, greater_than_expr):
        left = self._visit(greater_than_expr.left)
        right = self._visit(greater_than_expr.right)
        return left.greater_than_equals(right)

    @vis.visitor(ast.LessThanExpr)
    def _visit(self, less_than_expr):
        left = self._visit(less_than_expr.left)
        right = self._visit(less_than_expr.right)
        return left.less_than(right)

    @vis.visitor(ast.LessThanOrEqualExpr)
    def _visit(self, less_than_expr):
        left = self._visit(less_than_expr.left)
        right = self._visit(less_than_expr.right)
        return left.less_than_equals(right)

    @vis.visitor(ast.DecimalExpr)
    def _visit(self, decimal_expr):
        return values.Decimal(decimal_expr.value)

    @vis.visitor(ast.IntegerExpr)
    def _visit(self, integer_expr):
        return values.Integer(integer_expr.value)

    @vis.visitor(ast.StringExpr)
    def _visit(self, string_expr):
        return values.String(string_expr.value)

    @vis.visitor(ast.BooleanExpr)
    def _visit(self, boolean_expr):
        return values.Boolean.build(boolean_expr.value)

    @vis.visitor(ast.ListExpr)
    def _visit(self, list_expr):
        vs = []
        for v in list_expr.value:
            nv = self._visit(v)
            vs.append(nv)
        return values.List(vs)

    @vis.visitor(ast.NodeTypeExpr)
    def _visit(self, node_type_expr):
        return values.NodeType(node_type_expr.value)

    @vis.visitor(ast.VariableExpr)
    def _visit(self, variable_expr):
        return values.Node(self._context.get_node_by_id(variable_expr.name))

    @vis.visitor(ast.Node)
    def _visit(self, expr):
        return expr

    @vis.visitor(ast.IsExpr)
    def _visit(self, is_expr):
        node_expr = self._visit(is_expr.left)
        type_expr = self._visit(is_expr.right)
        return node_expr.is_(type_expr)

    @vis.visitor(ast.MatchExpr)
    def _visit(self, match_expr):
        operand = self._visit(match_expr.left)
        if not operand.value:
            return values.Boolean.TRUE
        regex = self._visit(match_expr.right)
        pattern = re.compile(regex.value)
        result = pattern.findall(operand.value)
        return values.Boolean.build(result)

    @vis.visitor(ast.InExpr)
    def _visit(self, in_expr):
        operand = self._visit(in_expr.left)
        list_ = self._visit(in_expr.right)
        return operand.in_(list_)

    @vis.visitor(ast.PropertyExpr)
    def _visit(self, prop_expr):
        node = self._visit(prop_expr.operand)
        successful, result = node.get_property(prop_expr.value)
        if not successful:
            msg = ''.join(['Error on line ', str(prop_expr.line), ': the matched CSS node of type \'',
                           node.value.get_type(), '\' does not have a property \'', prop_expr.value, '\''])
            raise InvalidPropertyException(msg)
        return result

    @vis.visitor(ast.MethodExpr)
    def _visit(self, method_expr):
        node = self._visit(method_expr.operand)
        argument = self._visit(method_expr.argument)
        successful, result = node.get_method(method_expr.value, argument.value)
        if not successful:
            msg = ''.join(['Error on line ', str(method_expr.line), ': the matched CSS node of type \'',
                           node.value.get_type(), '\' does not have a property \'', method_expr.value, '\''])
            raise InvalidPropertyException(msg)
        return result

    @vis.visitor(ast.ContainsExpr)
    def _visit(self, contains_expr):
        node_value = self._visit(contains_expr.operand)
        for d in self._context.pattern_matcher.find_descendants_that_match(node_value.value, contains_expr.argument):
            return values.Boolean.TRUE
        return values.Boolean.FALSE

    @vis.visitor(ast.ContainsAllExpr)
    def _visit(self, contains_all_expr):
        node_value = self._visit(contains_all_expr.operand)
        list_value = contains_all_expr.argument
        result = self._context.pattern_matcher.find_all(node_value.value, list_value.value)
        return values.Boolean.build(result)

    @vis.visitor(ast.ContainsAnyExpr)
    def _visit(self, contains_any_expr):
        node_value = self._visit(contains_any_expr.operand)
        list_value = contains_any_expr.argument
        result = self._context.pattern_matcher.find_any(node_value.value, list_value.value)
        return values.Boolean.build(result)

    @vis.visitor(ast.CountExpr)
    def _visit(self, count_expr):
        node_value = self._visit(count_expr.operand)
        count = 0
        for _ in self._context.pattern_matcher.find_descendants_that_match(node_value.value, count_expr.argument):
            count += 1
        return values.Integer(count)

    @vis.visitor(ast.NextSiblingExpr)
    def _visit(self, next_sibling):
        node_value = self._visit(next_sibling.operand)
        node = self._context.pattern_matcher.find_next_sibling(node_value.value)
        if node:
            return values.Node(node)
        return values.NonExistentNode.VALUE

    @vis.visitor(ast.PreviousSiblingExpr)
    def _visit(self, prev_sibling):
        node_value = self._visit(prev_sibling.operand)
        node = self._context.pattern_matcher.find_previous_sibling(node_value.value)
        if node:
            return values.Node(node)
        return values.NonExistentNode.VALUE

    @vis.visitor(ast.BeforeExpr)
    def _visit(self, before):
        operand_node_value = self._visit(before.operand)
        _filter = self._context.pattern_matcher.filter
        matcher = csscoco.lang.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_before_node(before.argument, operand_node_value.value)
        return values.Boolean.build(match)

    @vis.visitor(ast.BetweenExpr)
    def _visit(self, between):
        left_node_value = self._visit(between.operand)
        right_node_value = self._visit(between.second_operand)
        _filter = self._context.pattern_matcher.filter
        matcher = csscoco.lang.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_between_nodes(between.argument, left_node_value.value, right_node_value.value)
        return values.Boolean.build(match)

    @vis.visitor(ast.AfterExpr)
    def _visit(self, after):
        operand_node_value = self._visit(after.operand)
        _filter = self._context.pattern_matcher.filter
        matcher = csscoco.lang.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_after_node(after.argument, operand_node_value.value)
        return values.Boolean.build(match)


class InvalidPropertyException(Exception):
    def __init__(self, message):
        super(InvalidPropertyException, self).__init__()
        self.message = message