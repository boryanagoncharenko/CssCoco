import coco.ast.ast as ast
import coco.analysis.values as values
import coco.visitor_decorator as vis

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
        return self.visit(and_expr.left) and self.visit(and_expr.right)

    @vis.visitor(ast.EqualsExpr)
    def visit(self, equals_expr):
        return self.visit(equals_expr.left) == self.visit(equals_expr.right)

    @vis.visitor(ast.GreaterThanExpr)
    def visit(self, greater_than_expr):
        return self.visit(greater_than_expr.left) > self.visit(greater_than_expr.right)

    @vis.visitor(ast.VariableExpr)
    def visit(self, variable_expr):
        node = self._context.retrieve_node(variable_expr.value_string)
        return values.Node(node)

    @vis.visitor(ast.ImplicitVariableExpr)
    def visit(self, implicit_variable_expr):
        node = self._context.retrieve_node('current')
        return values.Node(node)

    @vis.visitor(ast.IntegerExpr)
    def visit(self, integer_expr):
        return values.Integer(integer_expr.value)

    @vis.visitor(ast.StringExpr)
    def visit(self, string_expr):
        return values.String(string_expr.value)

    @vis.visitor(ast.BooleanExpr)
    def visit(self, boolean_expr):
        return values.build_bool(boolean_expr.value)

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
        real_bool = node_type_value.is_node_of_type(node_value)
        return values.build_bool(real_bool)

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

    # @vis.visitor(ast.ConstantExpr)
    # def visit(self, contains_expr):
    #     node_value = self.operand.evaluate(context)
    #     node_value_type = self.argument.evaluate(context)
    #     for d in context.pattern_matcher.find_descendant(node_value.value, node_value_type):
    #         return True
    #     return False
    #
    # @vis.visitor(ast.CountExpr)
    # def visit(self, count_expr):
    #     node_value = self.operand.evaluate(context)
    #     count = sum(1 for _ in context.pattern_matcher.find_descendant(node_value.value, self.argument))
    #     return IntValue(count)

