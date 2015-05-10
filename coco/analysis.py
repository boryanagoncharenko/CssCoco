import coco.ast  as  ast
import coco.visitor_decorator as vis


class TypeChecker:
    pass


class Evaluator():

    @staticmethod
    def evaluate(ast):
        e = Evaluator()
        return e.__eval(ast)

    def __eval(self, ast):
        self.visit(ast)

    @vis.visitor(ast.Sheet)
    def visit(self, node):
        for child in node.get_children():
            self.visit(child)

    @vis.visitor(ast.RequireRule)
    def visit(self, node):
        pass
