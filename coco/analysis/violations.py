import coco.ast.ast as ast
import coco.analysis.expressions as expr
import coco.visitor_decorator as vis


class ViolationsFinder(object):

    def __init__(self, tree):
        self.tree = tree

    @staticmethod
    def find(sheet, tree):
        pass

    @vis.visitor(ast.Sheet)
    def visit(self, sheet):
        for c in sheet.contexts:
            self.visit(c)

    @vis.visitor(ast.SemanticContext)
    def visit(self, semantic_context):
        for c in semantic_context.conventions:
            self.visit(c)

    @vis.visitor(ast.FindRequireConvention)
    def visit(self, find_require):
        pass

    @vis.visitor(ast.ForbidConvention)
    def visit(self, forbid):
        pass

    @vis.visitor(ast.FindForbidConvention)
    def visit(self, find_forbid):
        pass


class ConventionsEvaluator(object):

    def __init__(self, convention, exceptions, tree):
        self.convention = convention
        self.exceptions = exceptions
        self.tree = tree

    @staticmethod
    def evaluate(convention, exceptions, tree):
        # get the patterns of nodes for descriptors
        # evaluate the constraint and log the violations
        evaluator = ConventionsEvaluator(convention, exceptions, tree)
        return evaluator._evaluate()

    def _evaluate(self):
        matcher = ast.PatternMatcher(None)
        for id_node_table in matcher.find_pattern_occurrences(self.tree, self.convention.target_pattern):
            res = self.visit(self.convention, id_node_table)
            print(res)

    @vis.visitor(ast.FindRequireConvention)
    def visit(self, find_require, id_node_table):
        return expr.ExprEvaluator.evaluate(find_require.constraint, id_node_table)

    @vis.visitor(ast.ForbidConvention)
    def visit(self, forbid, id_node_table):
        return True

    @vis.visitor(ast.FindForbidConvention)
    def visit(self, find_forbid, id_node_table):
        return expr.ExprEvaluator.evaluate(find_forbid.constraint, id_node_table)


