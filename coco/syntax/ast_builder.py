from coco.ast.ast import *
from coco.syntax.cocoParser import *
from coco.syntax.cocoVisitor import cocoVisitor
from antlr4.tree.Tree import *


class CocoCustomVisitor(cocoVisitor):

    identifiers = set()
    eval_target = False

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
        if ctx.name.text == 'Semantic':
            return SemanticContext(conventions, [])
        raise NotImplementedError()

    def visitDeclaration(self, ctx):
        # A declaration currently is only convention, so go there directly
        return self.visitConvention(ctx.children[0])

    def visitConvention(self, ctx):
        self.eval_target = True
        target = self.visitPattern(ctx.target)
        self.eval_target = False
        message = self.visitMessage(ctx.msg)

        if self.is_forbid_convention(ctx):
            return ForbidConvention(target, message=message)

        if self.is_require_convention(ctx):
            self.push_identifiers(target)
            requirement = self.visitAttr_expression(ctx.requirement)
            self.pop_identifiers()
            return FindRequireConvention(target, message=message, constraint=requirement)

        raise NotImplementedError('Unknown convention type')

    def push_identifiers(self, target):
        for wrapper in target.all_descs:
            if wrapper.identifier:
                self.identifiers.add(wrapper.identifier)

    def pop_identifiers(self):
        self.identifiers = set()

    def is_forbid_convention(self, ctx):
        return ctx.children[0].symbol.text == 'forbid'

    def is_require_convention(self, ctx):
        return ctx.children[0].symbol.text == 'find' and \
               ctx.children[2].symbol.text == 'require'

    def visitMessage(self, ctx):
        return self.unescape_quotes(ctx.children[1].symbol.text)

    def visitPattern(self, ctx):
        wrappers = []
        for child in ctx.children:
            if type(child) is cocoParser.NodeContext:
                wrapper = self.visitNode(child)
                wrappers.append(wrapper)
        relations = Relations()
        if len(wrappers) > 1:
            for i in range(0, len(wrappers)-1):
                relation = ctx.children[i*2+1]
                if relation.symbol.text == 'in':
                    relations.register_relation(wrappers[i+1], IsAncestorOfRelation(wrappers[i]))

        return PatternExpr(wrappers[-1], wrappers, relations)

    def visitNode(self, ctx):
        has_identifier, identifier = self.extract_identifier(ctx.children)
        i = 2 if has_identifier else 0
        node_desc = self.get_node_desc(ctx.children[i])
        attr_expr = None
        if len(ctx.children) > i+1:
            attr_expr = self.visitAttr_expression(ctx.children[i+1].children[1])
        return NodeExprWrapper(node_desc, attr_expr=attr_expr, identifier=identifier)

    def visitCall_expression(self, ctx):
        identifier = ctx.call.text
        if identifier in self.identifiers:
            return VariableExpr(identifier)
        if identifier == 'lowercase':
            return StringExpr('^[^A-Z]+$')
        if identifier == 'shorten':
            return StringExpr('(?P<gr1>[0-9a-f])(?P=gr1)(?P<gr2>[0-9a-f])(?P=gr2)(?P<gr3>[0-9a-f])(?P=gr3)')

        operand = VariableExpr('')
        if ctx.operand is not None:
            operand = self.visitCall_expression(ctx.operand)

        argument = self.visit_argument(ctx)
        if argument:
            if identifier == 'contains-all':
                return ContainsAllExpr(operand, argument)
            return MethodExpr(operand, ctx.call.text, argument)
        return PropertyExpr(operand, ctx.call.text)

    def visitAttr_expression(self, ctx):

        if self.is_unary(ctx):
            return self.visit_unary_attr_expr(ctx)

        if self.is_binary(ctx):
            return self.visit_binary_attr_expr(ctx)

        if ctx.call:
            return self.visitCall_expression(ctx.call)

        if ctx.primary_int is not None:
            return DecimalExpr(int(ctx.primary_int.text))

        if ctx.primary_str is not None:
            return StringExpr(self.unescape_quotes(ctx.primary_str.text))

        if ctx.primary_list is not None:
            return self.visitList_(ctx.primary_list)

    def visit_argument(self, ctx):
        if ctx.argument is not None:
            return self.visitAttr_expression(ctx.argument)
        if ctx.argument2 is not None:
            return self.visitNode(ctx.argument2)
        return None

    def is_unary(self, ctx):
        return ctx.operand is not None and ctx.operator is not None

    def visit_unary_attr_expr(self, ctx):
        operand = self.visitAttr_expression(ctx.operand)
        operator = ctx.operator.text
        if operator == 'not':
            return NotExpr(operand)
        if operator == '-':
            return UnaryMinusExpr(operand)
        raise NotImplementedError()

    def is_binary(self, ctx):
        return ctx.left is not None

    def visit_binary_attr_expr(self, ctx):
        operator = ctx.operator.text
        left = self.visitAttr_expression(ctx.left)
        right = None
        if operator == 'is':
            right = self.visitType_expression(ctx.right)
        else:
            right = self.visitAttr_expression(ctx.right)

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
            return InExpr(left, right)
        if operator == 'match':
            return MatchExpr(left, right)
        if operator == 'is':
            return IsExpr(left, right)

        raise ValueError('Unknown operator')

    def visitList_(self, ctx):
        result = []
        for child in ctx.children:
            if type(child) is cocoParser.List_elementContext:
                element = self.visitList_element(child)
                result.append(element)
        return ListExpr(result)

    def visitList_element(self, ctx):
        if ctx.element_id is not None:
            raise NotImplementedError()

        if ctx.element_int is not None:
            return int(ctx.element_int.text)

        if ctx.element_str is not None:
            return StringExpr(self.unescape_quotes(ctx.element_str.text))

        if ctx.element_desc is not None:
            return self.visitNode(ctx)

        raise ValueError('Unknown list element')

    def extract_identifier(self, children):
        assert children
        if len(children) < 2:
            return False, None
        if type(children[0]) is TerminalNodeImpl and type(children[1]) is TerminalNodeImpl:
            identifier = children[0].symbol.text
            return True, identifier
        return False, None

    def visitType_expression(self, ctx):
        if ctx.parenthesis:
            return self.visitType_expression(ctx.parenthesis)
        if ctx.operand:
            operand = self.visitType_expression(ctx.operand)
            return NotExpr(operand)
        if ctx.left:
            left = self.visitType_expression(ctx.left)
            right = self.visitType_expression(ctx.right)
            if ctx.operator.text == 'and':
                return AndExpr(left, right)
            if ctx.operator.text == 'or':
                return OrExpr(left, right)
        if ctx.primary:
            return NodeTypeExpr(ctx.primary)
        raise ValueError('Unknown type expression')


    def get_node_desc(self, ctx):
        lambda_string = self.get_type_expression_string(ctx)
        lambda_ = eval('lambda n: ' + lambda_string)
        return NodeDescriptor(func=lambda_)

    def get_type_expression_string(self, ctx):
        if ctx.parenthesis:
            return self.get_type_expression_string(ctx.children[1])

        if ctx.operand:
            return 'not (' + self.get_type_expression_string(ctx.operand) + ')'

        if ctx.left:
            left = self.get_type_expression_string(ctx.left)
            right = self.get_type_expression_string(ctx.right)
            return ''.join([left, ' ', ctx.operator.text, ' ', right])

        assert ctx.primary
        return ''.join(['\'', ctx.primary.text, '\' in n.search_labels'])

    def unescape_quotes(self, string):
        if len(string) < 2:
            return string
        result = string[1:-1]
        return result.replace('\\\'', '\'')