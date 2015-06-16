import re
import coco.ast.ast as ast
import coco.analysis.values as values
import coco.visitor_decorator as vis
import coco


class EvaluationContext(object):
    def __init__(self, pattern_matcher):
        self.pattern_matcher = pattern_matcher

    def get_node_by_id(self, identifier):
        raise NotImplementedError()

    def get_node_by_desc(self, desc):
        raise NotImplementedError()


class ExprContext(EvaluationContext):
    def __init__(self, pattern_matcher, node):
        super(ExprContext, self).__init__(pattern_matcher)
        assert node
        self._node = node

    def get_node_by_id(self, identifier):
        return self._node

    def get_node_by_desc(self, desc):
        return self._node


class ConstraintContext(EvaluationContext):
    def __init__(self, pattern_matcher, id_to_node_table):
        super(ConstraintContext, self).__init__(pattern_matcher)
        self._id_node_table = id_to_node_table

    def get_node_by_id(self, identifier):
        for desc in self._id_node_table:
            if desc.identifier == identifier:
                return self._id_node_table[desc]
        raise ValueError('Identifier not in context')

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

    @vis.visitor(ast.OrExpr)
    def visit(self, or_expr):
        return self.visit(or_expr.left) or self.visit(or_expr.right)

    @vis.visitor(ast.AndExpr)
    def visit(self, and_expr):
        left = self.visit(and_expr.left)
        if left.is_false():
            return values.Boolean.FALSE
        right = self.visit(and_expr.right)
        return left.and_(right)

    @vis.visitor(ast.EqualsExpr)
    def visit(self, equals_expr):
        left = self.visit(equals_expr.left)
        right = self.visit(equals_expr.right)
        return left.equals(right)

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
    def visit(self, integer_expr):
        return values.Decimal(integer_expr.value)

    @vis.visitor(ast.StringExpr)
    def visit(self, string_expr):
        return values.String(string_expr.value)

    @vis.visitor(ast.BooleanExpr)
    def visit(self, boolean_expr):
        return values.Boolean.build(boolean_expr.value)

    @vis.visitor(ast.ListExpr)
    def visit(self, list_expr):
        return values.List(list_expr.value)

    @vis.visitor(ast.NodeTypeExpr)
    def visit(self, node_type_expr):
        return values.NodeType(node_type_expr.value)

    @vis.visitor(ast.VariableExpr)
    def visit(self, variable_expr):
        return values.Node(self._context.get_node_by_id(variable_expr.variable_name))

    @vis.visitor(ast.NodeExprWrapper)
    def visit(self, expr):
        return expr

    @vis.visitor(ast.IsExpr)
    def visit(self, is_expr):
        node_expr = self.visit(is_expr.left)
        type_expr = self.visit(is_expr.right)
        return node_expr.is_(type_expr)
        # if not wrapper.type_desc.is_node_match(operand.value):
        #     return values.Boolean.FALSE
        # if wrapper.attr_expr:
        #     newContext = ExprContext(self._context.pattern_matcher, operand.value)
        #     return ExprEvaluator.evaluate(wrapper.attr_expr, newContext)
        # return values.Boolean.FALSE

    @vis.visitor(ast.MatchExpr)
    def visit(self, match_expr):
        operand = self.visit(match_expr.operand)
        if not operand.value:
            return values.Boolean.TRUE
        regex = self.visit(match_expr.regex)
        pattern = re.compile(regex.value)
        result = pattern.findall(operand.value)
        return values.Boolean.build(result)

    @vis.visitor(ast.ApiCallExpr)
    def visit(self, api_call_expr):
        node = self.visit(api_call_expr.operand)
        real_node = node.value
        property_value = real_node.invoke_method(api_call_expr.property_string)
        return property_value

    @vis.visitor(ast.ApiCallExprWithArg)
    def visit(self, api_call_args_expr):
        node = self.visit(api_call_args_expr.operand)
        real_node = node.value
        property_value = real_node.invoke_method_with_arg(api_call_args_expr.property_string, api_call_args_expr.argument)
        return property_value

    @vis.visitor(ast.ContainsExpr)
    def visit(self, contains_expr):
        node_value = self.visit(contains_expr.operand)
        for d in self._context.pattern_matcher.find_descendants_that_match(node_value.value, ast.NodeExprWrapper(contains_expr.argument)):
            return values.Boolean.TRUE
        return values.Boolean.FALSE

    @vis.visitor(ast.ContainsAllExpr)
    def visit(self, contains_all_expr):
        node_value = self.visit(contains_all_expr.operand)
        list_value = contains_all_expr.argument
        result =  self._context.pattern_matcher.find_all(node_value.value, list_value.value)
        return values.Boolean.build(result)

    @vis.visitor(ast.CountExpr)
    def visit(self, count_expr):
        node_value = self.visit(count_expr.operand)
        count = 0
        for _ in self._context.pattern_matcher.find_descendants_that_match(node_value.value, ast.NodeExprWrapper(count_expr.argument)):
            count += 1
        return values.Decimal(count)

    @vis.visitor(ast.NextSiblingExpr)
    def visit(self, next_sibling):
        node_value = self.visit(next_sibling.operand)
        node = self._context.pattern_matcher.find_next_adjacent_sibling(node_value.value)
        if node:
            return values.Node(node)
        return values.Undefined.VALUE

    @vis.visitor(ast.BeforeExpr)
    def visit(self, before):
        operand_node_value = self.visit(before.operand)
        _filter = self._context.pattern_matcher._filter
        matcher = coco.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_before_node(before.variation, operand_node_value.value)
        return values.Boolean.build(match)

    @vis.visitor(ast.BetweenExpr)
    def visit(self, between):
        left_node_value = self.visit(between.operand)
        right_node_value = self.visit(between.second_operand)
        _filter = self._context.pattern_matcher._filter
        matcher = coco.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_between_nodes(between.variation, left_node_value.value, right_node_value.value)
        return values.Boolean.build(match)

    @vis.visitor(ast.AfterExpr)
    def visit(self, after):
        operand_node_value = self.visit(after.operand)
        _filter = self._context.pattern_matcher._filter
        matcher = coco.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_after_node(after.variation, operand_node_value.value)
        return values.Boolean.build(match)

