import coco.ast.ast as cocoast
import coco.analysis.expressions as expr
import coco.analysis.values as values
import coco.analysis.violations as violations


def test_eval_integer_expr():
    e = cocoast.IntegerExpr(1)
    context = expr.ExprEvaluationContext(None, None)
    res_value = expr.ExprEvaluator.evaluate(e, context)
    assert type(res_value) is values.Integer and res_value.value == 1


def real_case_expr():

    attr_expr3 = cocoast.IsExpr(cocoast.ImplicitVariableExpr(), cocoast.NodeTypeExpr(type_string='declaration'))
    attr_expr2 = cocoast.EqualsExpr(cocoast.CountExpr(cocoast.ImplicitVariableExpr(), attr_expr3), cocoast.IntegerExpr(0))

    attr_expr1 = cocoast.IsExpr(cocoast.ImplicitVariableExpr(), cocoast.NodeTypeExpr(type_string='ruleset'))
    rule_node = cocoast.NodeExprWrapper(cocoast.AndExpr(attr_expr1, attr_expr2))

    relations = cocoast.Relations()
    pattern = cocoast.PatternExpr(rule_node, [rule_node], relations)

    convention = cocoast.ForbidConvention(pattern, "Do leave empty ruleset")
    context = cocoast.SemanticContext([convention], None)
    sheet = cocoast.Sheet([context])

    # violations.ViolationsFinder.find(sheet, css_tree)