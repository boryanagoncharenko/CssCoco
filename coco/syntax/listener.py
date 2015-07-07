from coco.ast.ast import *
from coco.syntax.cocoListener import cocoListener
from coco.syntax.cocoVisitor import cocoVisitor
from antlr4.tree.Tree import *

class CocoCustomListener(cocoListener):

    def enterStylesheet(self, ctx):
        set = ConventionSet(None)

    def exitStylesheet(self, ctx):
        pass

    def enterContext(self, ctx):
        pass

    def exitContext(self, ctx):
        pass


class CocoCustomVisitor(cocoVisitor):

    def visitStylesheet(self, ctx):
        contexts = []
        for contextCtx in ctx.children:
            contexts.append(self.visitContext(contextCtx))
        return ConventionSet(contexts)

    def visitContext(self, ctx):
        conventions = []
        for i in range(2, len(ctx.children)-1):
            convention_ctx = ctx.children[i]
            conventions.append(self.visitDeclaration(convention_ctx))
        return Context(conventions, [])

    def visitDeclaration(self, ctx):
        # A declaration currently is only convention, so go there directly
        return self.visitConvention(ctx.children[0])

    def visitConvention(self, ctx):
        target = self.visitPattern(ctx.children[1])
        message = self.visitMessage(ctx.children[2])
        if ctx.children[0].symbol.text == 'forbid':
            return ForbidConvention(target, message=message)
        return FindRequireConvention(target, message=message, constraint=None)

    def visitMessage(self, ctx):
        return self.unescape_quotes(ctx.children[1].symbol.text)

    def visitPattern(self, ctx):
        node_wrapper = self.visitNode(ctx.children[0])
        return PatternExpr(node_wrapper, [node_wrapper], Relations())

    def visitNode(self, ctx):
        has_identifier, identifier = self.extract_identifier(ctx.children)
        i = 2 if has_identifier else 0
        node_desc = self.get_node_desc(ctx.children[i])
        attr_expr = None
        if len(ctx.children) > i+1:
            attr_expr = self.visit_attr_expr(ctx.children[i+1].children[1])
        return NodeExprWrapper(node_desc, attr_expr=attr_expr, identifier=identifier)

    def visit_attr_expr(self, ctx):
        if ctx.operand is not None:
            return self.visit_unary_attr_expr(ctx)

        if ctx.left is not None:
            return self.visit_binary_attr_expr(ctx)

        if ctx.primary_id is not None:
            return ApiCallExpr(VariableExpr(''), ctx.primary_id.text)

        if ctx.primary_int is not None:
            raise NotImplementedError()

        if ctx.primary_str is not None:
            return StringExpr(self.unescape_quotes(ctx.primary_str.text))

    def visit_unary_attr_expr(self, ctx):
        operand = self.visit_attr_expr(ctx.operand)

        if ctx.operator.text == 'not':
            return NotExpr(operand)
        raise NotImplementedError()

    def visit_binary_attr_expr(self, ctx):
        operator = ctx.operator.text
        left = self.visit_attr_expr(ctx.left)
        right = self.visit_attr_expr(ctx.right)

        if operator == '==':
            return EqualsExpr(left, right)
        if operator == '!=':
            return NotEqualsExpr(left, right)
        if operator == '<':
            return LessThanExpr(left, right)
        if operator == '>':
            return GreaterThanExpr(left, right)
        if operator == '<=':
            return LessThanOrEqExpr(left, right)
        if operator == '>=':
            return GreaterThanOrEqExpr(left, right)

        if operator == 'and':
            return AndExpr(left, right)
        if operator == 'or':
            return OrExpr(left, right)

        if operator == 'in':
            raise NotImplementedError()
        if operator == 'match':
            return MatchExpr(left, right)
        if operator == 'is':
            return IsExpr(left, right)

        raise ValueError()

    def extract_identifier(self, children):
        assert children
        if len(children) < 2:
            return False, None
        if type(children[0]) is TerminalNodeImpl and type(children[1]) is TerminalNodeImpl:
            identifier = children[0].symbol.text
            return True, identifier
        return False, None

    def get_node_desc(self, ctx):
        lambda_string = self.visit_type_expr(ctx)
        lambda_ = eval('lambda n: ' + lambda_string)
        return NodeDescriptor(func=lambda_)

    def visit_type_expr(self, ctx):
        if ctx.parenthesis is not None:
            return self.visit_type_expr(ctx.children[1])

        if ctx.operand is not None:
            return 'not (' + self.visit_type_expr(ctx.operand) + ')'

        if ctx.left is not None:
            left = self.visit_type_expr(ctx.left)
            right = self.visit_type_expr(ctx.right)
            return ''.join([left, ' ', ctx.operator.text, ' ', right])

        assert ctx.primary is not None
        return ''.join(['\'', ctx.primary.text, '\' in n.search_labels'])

    def unescape_quotes(self, string):
        if len(string) < 2:
            return string
        result = string[1:-1]
        return result.replace('\\\'', '\'')