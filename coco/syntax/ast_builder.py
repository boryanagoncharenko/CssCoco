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
        if ctx.name.text == 'Whitespace':
            return WhitespaceContext(conventions, [])
        raise NotImplementedError()

    def visitDeclaration(self, ctx):
        # A declaration currently is only convention, so go there directly
        return self.visitConvention(ctx.children[0])

    def visitConvention(self, context):
        if self.is_require_convention(context):
            return self.visit_require_convention(context)

        self.eval_target = True
        target = self.visitPattern(context.target)
        self.eval_target = False

        message = self.visitMessage(context.msg)

        if self.is_forbid_convention(context):
            return ForbidConvention(target, message=message)

        if self.is_find_require_convention(context):
            self.push_identifiers(target)
            requirement = self.visitAttr_expression(context.requirement)
            self.pop_identifiers()
            return FindRequireConvention(target, message=message, constraint=requirement)

        raise NotImplementedError('Unknown convention type')

    def visit_require_convention(self, context):
        succeeded, target = self.interpolate_target(context.requirement)
        if not succeeded:
            raise ValueError('Invalid convention target. Consider breaking the convention to simpler patterns')
        message = self.visitMessage(context.msg)

        self.push_identifiers(target)
        requirement = self.visitAttr_expression(context.requirement)
        self.pop_identifiers()

        return FindRequireConvention(target, message=message, constraint=requirement)

    def interpolate_target(self, context):
        if context.operator:
            operator = context.operator.text
            wrappers = []
            if operator == 'after' or operator == 'before':
                right = self.visit_whitespace_argument(context.right, 'a1')
                wrappers.append(right)
            if operator == 'between':
                first = self.visit_whitespace_argument(context.first, 'a1')
                second = self.visit_whitespace_argument(context.second, 'a2')

                wrappers.append(first)
                wrappers.append(second)
            return True, SequencePatternExpr(wrappers)
        return False, None

    def visit_whitespace_argument(self, context, identifier):
        if context.abstract:
            return self.visit_abstract_node_decl(context.abstract, identifier)
        # if context.call:
        #     return self.visitCall_expression(context.call)
        if context.string_:
            raise NotImplementedError()
        raise ValueError('Unknown whitespace argument')

    def push_identifiers(self, target):
        for wrapper in target.all_descs:
            if wrapper.has_identifier():
                self.identifiers.add(wrapper.identifier)

    def pop_identifiers(self):
        self.identifiers = set()

    def is_forbid_convention(self, ctx):
        return ctx.children[0].symbol.text == 'forbid'

    def is_find_require_convention(self, ctx):
        return ctx.children[0].symbol.text == 'find' and \
               ctx.children[2].symbol.text == 'require'

    def is_require_convention(self, ctx):
        return ctx.children[0].symbol.text == 'require'

    def visitMessage(self, ctx):
        return self.unescape_quotes(ctx.children[1].symbol.text)

    def visitPattern(self, ctx):
        wrappers = []
        for child in ctx.children:
            if type(child) is cocoParser.NodeContext:
                wrapper = self.visitNode(child)
                wrappers.append(wrapper)
        if ctx.semantic:
            relations = Relations()
            if len(wrappers) > 1:
                for i in range(0, len(wrappers)-1):
                    # relation = ctx.children[i*2+1]
                    if ctx.relation.text == 'in':
                        relations.register_relation(wrappers[i+1], IsAncestorOfRelation(wrappers[i]))
                    if ctx.relation.text == 'next-to':
                        return SequencePatternExpr(wrappers)
            return PatternExpr(wrappers[-1], wrappers, relations)
        # if ctx.whitespace:
        #     return SequencePatternExpr(wrappers)
        raise NotImplementedError()

    def visitNode(self, ctx):
        if ctx.abstract and ctx.decl:
            return self.visit_abstract_node_decl(ctx.abstract, ctx.decl.text)
        if ctx.abstract:
            return self.visitAbstract_node(ctx.abstract)
        if ctx.parse:
            return self.visitParse_node(ctx.parse)
        raise ValueError('Unknown node')

    def visitAbstract_node(self, ctx):
        node_descriptor, attr_expression = self.get_type_and_attr_expr(ctx)
        return NodeExprWrapper(node_descriptor, attr_expr=attr_expression)

    def visit_abstract_node_decl(self, ctx, identifier):
        node_descriptor, attr_expression = self.get_type_and_attr_expr(ctx)
        return NodeExprWrapperWithId(node_descriptor, identifier, attr_expr=attr_expression)

    def get_type_and_attr_expr(self, ctx):
        node_descriptor = self.get_node_desc(ctx.node_type)
        if not ctx.constraint:
            return node_descriptor, None
        attr_expression = self.visitAttr_expression(ctx.constraint)
        return node_descriptor, attr_expression

    def visitParse_node(self, ctx):
        if ctx.parenthesis:
            return self.visitParse_node(ctx.parenthesis)
        if ctx.left:
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            return OrExpr(left, right)
        if ctx.primary:
            node_descriptor = self.get_node_desc(ctx)
            repeater = Repeater.DEFAULT
            if self.parse_node_has_constraint(ctx):
                repeater = self.get_parse_node_constraint(ctx)
            return NodeSequenceExprWrapper(node_descriptor, repeater)

    def parse_node_has_constraint(self, ctx):
        return ctx.lower or ctx.upper or ctx.exact

    def get_parse_node_constraint(self, ctx):
        if ctx.exact:
            exact = int(ctx.exact)
            return Repeater(exact, exact)
        if ctx.lower and ctx.upper:
            lower = int(ctx.lower)
            upper = int(ctx.upper)
            return Repeater(lower, upper)
        if ctx.lower:
            lower = int(ctx.lower)
            return Repeater(lower=lower)
        if ctx.upper:
            upper = int(ctx.upper)
            return Repeater(upper=upper)
        raise ValueError('Unknown parse node constraint')

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

        if ctx.parenthesis:
            return self.visitAttr_expression(self.parenthesis)

        if self.is_unary(ctx):
            return self.visit_unary_attr_expr(ctx)

        if ctx.operator and ctx.operator.text == 'is':
            pass

        if ctx.operator and ctx.operator.text in ['in', 'not in', 'match', 'not match']:
            pass

        if self.is_binary(ctx):
            return self.visit_binary_attr_expr(ctx)

        if ctx.primary_int is not None:
            return DecimalExpr(int(ctx.primary_int.text))

        if ctx.primary_str is not None:
            return StringExpr(self.unescape_quotes(ctx.primary_str.text))

        if ctx.primary_list is not None:
            return self.visitList_(ctx.primary_list)

        if ctx.call:
            return self.visitCall_expression(ctx.call)

        raise ValueError('Unknown attribute expression')

    def visit_argument(self, ctx):
        if ctx.argument is not None:
            return self.visitAttr_expression(ctx.argument)
        if ctx.abstract is not None:
            return self.visitNode(ctx.abstract)
        return None

    def is_unary(self, ctx):
        return ctx.operand and ctx.operator

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
        left = None
        if operator in ['before', 'after', 'between']:
            left = self.visitParse_node(ctx.left)
        else:
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
        if operator == 'not in':
            raise  NotImplementedError()
        if operator == 'match':
            return MatchExpr(left, right)
        if operator == 'not match':
            return NotExpr(MatchExpr(left, right))
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
            return self.visitAbstract_node(ctx.element_desc)
        raise ValueError('Unknown list element')

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
            return NodeTypeExpr(ctx.primary.text)
        raise ValueError('Unknown type expression')


    def get_node_desc(self, ctx):
        lambda_string = self.get_type_expression_string(ctx)
        lambda_ = eval('lambda n: ' + lambda_string)
        return NodeDescriptor(func=lambda_)

    def get_type_expression_string(self, ctx):
        if ctx.parenthesis:
            return self.get_type_expression_string(ctx.children[1])

        if ctx.left:
            left = self.get_type_expression_string(ctx.left)
            right = self.get_type_expression_string(ctx.right)
            return ''.join([left, ' ', ctx.operator.text, ' ', right])

        if ctx.primary:
            return ''.join(['\'', ctx.primary.text, '\' in n.search_labels'])

        if ctx.operand:
            return 'not (' + self.get_type_expression_string(ctx.operand) + ')'

        raise ValueError('Unknown type expression')

    def unescape_quotes(self, string):
        if len(string) < 2:
            return string
        result = string[1:-1]
        return result.replace('\\\'', '\'')