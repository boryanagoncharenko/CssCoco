from csscoco.lang.ast import ast as ast


# def test_eval_integer_expr():
#     e = ast.IntegerExpr(1)
#     context = expr.ExprContext(None, None)
#     res_value = expr.ExprEvaluator.evaluate(e, context)
#     assert type(res_value) is values.Integer and res_value.value == 1


def real_case_expr():

    attr_expr3 = ast.IsExpr(ast.ImplicitVariableExpr(), ast.NodeTypeExpr(type_string='declaration'))
    attr_expr2 = ast.EqualExpr(ast.CountExpr(ast.ImplicitVariableExpr(), attr_expr3), ast.IntegerExpr(0))

    attr_expr1 = ast.IsExpr(ast.ImplicitVariableExpr(), ast.NodeTypeExpr(type_string='ruleset'))
    rule_node = ast.Node(ast.AndExpr(attr_expr1, attr_expr2))

    relations = ast.NodeRelations()
    pattern = ast.Pattern(rule_node, [rule_node], relations)

    convention = ast.ForbidConvention(pattern, "Do leave empty ruleset")
    context = ast.SemanticContext([convention], None)
    sheet = ast.ConventionSet([context])

    # violations.ViolationsFinder.find(sheet, css_tree)