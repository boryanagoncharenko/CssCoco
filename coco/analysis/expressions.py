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
        return self.visit(greater_than_expr.left) > self.visit(greater_than_expr.right)

    @vis.visitor(ast.VariableExpr)
    def visit(self, variable_expr):
        node = self._context.get_node_by_id(variable_expr.value_string)
        return values.Node(node)

    @vis.visitor(ast.ImplicitVariableExpr)
    def visit(self, implicit_variable_expr):
        node = self._context.get_node_by_id('current')
        return values.Node(node)

    @vis.visitor(ast.IntegerExpr)
    def visit(self, integer_expr):
        return values.Integer(integer_expr.value)

    @vis.visitor(ast.StringExpr)
    def visit(self, string_expr):
        return values.String(string_expr.value)

    @vis.visitor(ast.BooleanExpr)
    def visit(self, boolean_expr):
        return values.Boolean.build(boolean_expr.value)

    @vis.visitor(ast.NodeTypeExpr)
    def visit(self, node_type_expr):
        return values.NodeType(node_type_expr.type, node_type_expr.value)

    @vis.visitor(ast.ListExpr)
    def visit(self, list_expr):
        return values.List(list_expr.value)

    @vis.visitor(ast.IsExpr)
    def visit(self, is_expr):
        node_value = self.visit(is_expr.left)
        node_type_value = self.visit(is_expr.right)
        real_bool = node_value.is_(node_type_value)
        return values.Boolean.build(real_bool)

    @vis.visitor(ast.ApiCallExpr)
    def visit(self, api_call_expr):
        node_value = self.visit(api_call_expr.operand)
        property_value = node_value.value.invoke_method(api_call_expr.property_string)
        return property_value

    @vis.visitor(ast.ApiCallExprWithArg)
    def visit(self, api_call_args_expr):
        node_value = self.visit(api_call_args_expr.operand)
        property_value = node_value.value.invoke_method_with_arg(api_call_args_expr.property_string,
                                                                 api_call_args_expr.argument)
        return property_value

    @vis.visitor(ast.ContainsExpr)
    def visit(self, contains_expr):
        node_value = self.visit(contains_expr.operand)
        for d in self._context.matcher.find_descendants_that_match(node_value.value, ast.NodeExprWrapper(contains_expr.argument)):
            return values.Boolean.TRUE
        return values.Boolean.FALSE

    @vis.visitor(ast.CountExpr)
    def visit(self, count_expr):
        node_value = self.visit(count_expr.operand)
        count = 0
        for _ in self._context.matcher.find_descendants_that_match(node_value.value, ast.NodeExprWrapper(count_expr.argument)):
            count += 1
        return values.Integer(count)

    @vis.visitor(ast.NextSiblingExpr)
    def visit(self, next_sibling):
        node_value = self.visit(next_sibling.operand)
        node = self._context.matcher.find_next_adjacent_sibling(node_value.value)
        if node:
            return values.Node(node)
        return values.Undefined.VALUE

    @vis.visitor(ast.BeforeExpr)
    def visit(self, before):
        operand_node_value = self.visit(before.operand)
        _filter = coco.analysis.pattern_matcher.VariationFilter(self._context.pattern_matcher.filter_seq)
        matcher = coco.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_before_node(before.variation, operand_node_value.value)
        return values.Boolean.build(match)

    @vis.visitor(ast.BetweenExpr)
    def visit(self, between):
        left_node_value = self.visit(between.operand)
        right_node_value = self.visit(between.second_operand)
        _filter = coco.analysis.pattern_matcher.VariationFilter(self._context.pattern_matcher.filter_seq)
        matcher = coco.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_between_nodes(between.variation, left_node_value.value, right_node_value.value)
        return values.Boolean.build(match)

    @vis.visitor(ast.AfterExpr)
    def visit(self, after):
        operand_node_value = self.visit(after.operand)
        _filter = coco.analysis.pattern_matcher.VariationFilter(self._context.pattern_matcher.filter_seq)
        matcher = coco.analysis.pattern_matcher.WhitespaceVariationMatcher(_filter)
        match = matcher.is_variation_after_node(after.variation, operand_node_value)
        return values.Boolean.build(match)

