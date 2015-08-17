import antlr4.tree.Tree as Tree

import csscoco.lang.ast.ast as ast
import csscoco.lang.syntax.cocoParser as Parser
from csscoco.lang.syntax.cocoVisitor import cocoVisitor
from csscoco.lang.common_ import ExprConstants


class CocoCustomVisitor(cocoVisitor):
    def __init__(self):
        super(CocoCustomVisitor, self).__init__()
        self.identifiers = set()

    def visitStylesheet(self, context):
        if not context.children:
            return ast.ConventionSet([])
        contexts = []
        for contextCtx in context.children:
            contexts.append(self.visitContext(contextCtx))
        return ast.ConventionSet(contexts)

    def visitContext(self, context):
        ignores = self.get_ignores(context)
        conventions = self.get_conventions(context)
        return ast.Context(conventions, ignores)

    def get_conventions(self, context):
        result = []
        start = 3 if context.ignore else 2
        # TODO: find why antlr does not support list of named tokens
        for i in range(start, len(context.children)-1):
            convention = self.visitConvention(context.children[i])
            result.append(convention)
        return result

    def get_ignores(self, context):
        result = []
        if not context.ignore:
            return result
        current_pattern = []
        for i in range(1, len(context.ignore.children)):
            child = context.ignore.children[i]
            if self.is_terminal(child):
                result.append(ast.SequencePattern(current_pattern))
                current_pattern = []
            else:
                node = self.visitWhitespace_node(child)
                current_pattern.append(node)
        if current_pattern:
            result.append(ast.SequencePattern(current_pattern))
        return result

    def is_terminal(self, node):
        # TODO: find why antlr does not support list of named tokens
        return type(node) is Tree.TerminalNodeImpl

    def visitConvention(self, context):
        message = self.visit_message(context)
        target = self.visitPattern(context.target)

        if self.is_forbid_convention(context):
            return ast.ForbidConvention(target, message)

        if context.find:
            self.push_identifiers(target)
            if context.where:
                constraint = self.visitLogic_expr(context.where)
                target = ast.PatternConstraintDescriptor(target.root, target.nodes, target.relations, constraint)
            constraint = self.visitLogic_expr(context.requirement)
            self.pop_identifiers()
            if self.is_require_convention(context):
                return ast.FindRequireConvention(target, description=message, constraint=constraint)
            return ast.FindForbidConvention(target, description=message, constraint=constraint)

        raise ValueError('Unknown convention type')

    def push_identifiers(self, target):
        for wrapper in target.nodes:
            if wrapper.has_identifier():
                self.identifiers.add(wrapper.identifier)

    def pop_identifiers(self):
        self.identifiers = set()

    def is_forbid_convention(self, context):
        return not context.find and context.action.text == 'forbid'

    def is_require_convention(self, context):
        return context.action.text == 'require'

    def visit_message(self, context):
        return self.unescape_quotes(context.message.text)

    def visitPattern(self, context):
        if context.simple:
            return self.handle_simple_pattern(context)
        return self.handle_fork_pattern(context)

    def handle_simple_pattern(self, context):
        if len(context.children) == 1:
            wrapper = self.visitNode_declaration(context.children[0])
            return ast.PatternDescriptor(wrapper, [wrapper], ast.NodeRelations.EMPTY)
        wrappers = self.get_wrappers(context)
        if self.is_vertical(context):
            return self.build_in_pattern(wrappers)
        return self.build_next_pattern(wrappers)

    def get_wrappers(self, context):
        wrappers = []
        step = 2 if self.is_vertical(context) else 1
        for i in range(0, len(context.children), step):
            wrapper = self.visitNode_declaration(context.children[i])
            wrappers.append(wrapper)
        return wrappers

    def is_vertical(self, context):
        return type(context.children[1]) is Tree.TerminalNodeImpl

    def build_in_pattern(self, wrappers):
        relations = ast.NodeRelations()
        for i in range(1, len(wrappers)):
            relations.register_relation(wrappers[i], ast.IsAncestorOf(wrappers[i-1]))
        return ast.PatternDescriptor(wrappers[-1], wrappers, relations)

    def build_next_pattern(self, wrappers):
        relations = ast.NodeRelations()
        for i in range(1, len(wrappers)):
            relations.register_relation(wrappers[i-1], ast.IsPreviousSiblingOf(wrappers[i]))
        return ast.SequencePattern(wrappers)

    def handle_fork_pattern(self, context):
        fork_wrappers = self.visitFork_pattern(context.fork)
        in_wrappers = []
        for i in range(2, len(context.children), 2):
            wrapper = self.visitNode_declaration(context.children[i])
            in_wrappers.append(wrapper)
        relations = ast.NodeRelations()
        for i in range(1, len(in_wrappers)):
            relations.register_relation(in_wrappers[i], ast.IsAncestorOf(in_wrappers[i-1]))
        for fork in fork_wrappers:
            relations.register_relation(in_wrappers[0], ast.IsAncestorOf(fork))
        return ast.PatternDescriptor(in_wrappers[-1], in_wrappers + fork_wrappers, relations)

    def visitFork_pattern(self, context):
        wrappers = []
        for i in range(1, len(context.children), 2):
            wrapper = self.visitNode_declaration(context.children[i])
            wrappers.append(wrapper)
        return wrappers

    def visitNode_declaration(self, context):
        if context.variable and context.node:
            return self.visit_semantic_node_with_id(context.node, context.variable.text)
        if context.node:
            return self.visitSemantic_node(context.node)
        raise ValueError('Unknown node declaration')

    def visit_semantic_node_with_id(self, context, variable):
        node_descriptor = self.get_node_descriptor(context.type_)
        line = context.type_.start.line
        if not context.constraint:
            return ast.Node(node_descriptor, line, identifier=variable)
        constraint = self.visitLogic_expr(context.constraint)
        return ast.Node(node_descriptor, line, identifier=variable, constraint=constraint)

    def visitSemantic_node(self, context):
        node_descriptor = self.get_node_descriptor(context.type_)
        line = context.type_.start.line
        if not context.constraint:
            return ast.Node(node_descriptor, line)
        constraint = self.visitLogic_expr(context.constraint)
        return ast.Node(node_descriptor, line, constraint)

    def visitLogic_expr(self, context):
        if context.parenthesis:
            return self.visitLogic_expr(context.parenthesis)
        if context.type_:
            return self.visitType_expr(context.type_)
        if context.call:
            return self.visitArithmetic_expr(context.call)

        operator = context.operator.text
        line = context.operator.line
        if operator == 'not':
            operand = self.visitLogic_expr(context.operand)
            return ast.NotExpr(operand, line)

        left = self.visitLogic_expr(context.left)
        right = self.visitLogic_expr(context.right)
        if operator == 'and':
            return ast.AndExpr(left, right, line)
        if operator == 'or':
            return ast.OrExpr(left, right, line)
        raise ValueError('Unknown expression')

    def visitType_expr(self, context):
        operator = context.operator.text
        line = context.operator.line
        if operator == 'is':
            operand = self.visitArithmetic_expr(context.operand)
            node_type = ast.NodeTypeExpr(context.type_.text)
            return ast.IsExpr(operand, node_type, line)
        variation = self.visitWhitespace_variation(context.variation)
        operand = self.get_type_expr_right(context.operand)
        if operator == 'before':
            return ast.BeforeExpr(operand, variation, line)
        if operator == 'after':
            return ast.AfterExpr(operand, variation, line)
        if operator == 'between':
            second_operand = self.get_type_expr_right(context.second_operand)
            return ast.BetweenExpr(operand, variation, second_operand, line)
        raise ValueError('Unknown expression')

    def get_type_expr_right(self, operand):
        return self.visitCall_expr(operand)

    def visitWhitespace_variation(self, context):
        sequences = []
        for i in range(0, len(context.children), 2):
            descriptor = self.visitWhitespace_node(context.children[i])
            sequences.append(ast.SequencePattern([descriptor]))
        return ast.WhitespaceVariation(sequences)

    def visitWhitespace_node(self, context):
        node_descriptor = self.get_ws_node_descriptor(context.type_.text)
        line = context.type_.line
        if context.quantifier:
            repeater = self.visitRepeater(context.quantifier)
            return ast.WhitespaceNode(node_descriptor, repeater, line)
        return ast.Node(node_descriptor, line)

    def visitRepeater(self, context):
        lower = -1
        upper = -1
        if context.exact:
            limit = int(context.exact.text)
            lower = limit
            upper = limit
        if context.lower:
            lower = int(context.lower.text)
        if context.upper:
            upper = int(context.upper.text)
        return ast.Repeater(lower=lower, upper=upper)

    def visitArithmetic_expr(self, context):
        if context.primary:
            return self.visitElement(context.primary)
        if context.call:
            return self.visitCall_expr(context.call)
        operator = context.operator.text
        line = context.operator.line
        if operator == '-':
            operand = self.visitArithmetic_expr(context.operand)
            return ast.UnaryMinusExpr(operand, line)
        if operator == '+':
            operand = self.visitArithmetic_expr(context.operand)
            return ast.UnaryPlusExpr(operand)

        left = self.visitArithmetic_expr(context.left)
        right = self.visitArithmetic_expr(context.right)
        return self.binary_arithmetic_expr(context, left, right, line)

    def binary_arithmetic_expr(self, context, left, right, line):
        operator = context.operator.text
        if operator == '==':
            return ast.EqualExpr(left, right, line)
        if operator == '!=':
            return ast.NotEqualExpr(left, right, line)
        if operator == '<':
            return ast.LessThanExpr(left, right, line)
        if operator == '>':
            return ast.GreaterThanExpr(left, right, line)
        if operator == '<=':
            return ast.LessThanOrEqualExpr(left, right, line)
        if operator == '>=':
            return ast.GreaterThanOrEqualExpr(left, right, line)

        if operator == 'in':
            return ast.InExpr(left, right, line)
        if operator == 'not in':
            return ast.NotExpr(ast.InExpr(left, right, line))
        if operator == 'match':
            return ast.MatchExpr(left, right, line)
        if operator == 'not match':
            return ast.NotExpr(ast.MatchExpr(left, right, line))
        raise ValueError('Unknown expression')

    def visitElement(self, context):
        if context.primary_bool:
            return ast.BooleanExpr(bool(context.primary_bool.text.lower() != 'false'), context.primary_bool.line)
        if context.primary_dec:
            return ast.DecimalExpr(float(context.primary_dec.text), context.primary_dec.line)
        if context.primary_int:
            return ast.IntegerExpr(int(context.primary_int.text), context.primary_int.line)
        if context.primary_str:
            return ast.StringExpr(self.unescape_quotes(context.primary_str.text), context.primary_str.line)
        if context.primary_list:
            return self.visitList_(context.primary_list)
        raise ValueError('Unknown element')

    def visitCall_expr(self, context):
        identifier = context.call.text.lower()
        line = context.call.line
        if identifier in self.identifiers or identifier == 'stylesheet':
            return ast.VariableExpr(identifier, line)
        if identifier == 'lowercase':
            return ast.StringExpr('^[^A-Z]+$', line)
        if identifier == 'shorten':
            return ast.StringExpr('(?P<gr1>[0-9a-f])(?P=gr1)(?P<gr2>[0-9a-f])(?P=gr2)(?P<gr3>[0-9a-f])(?P=gr3)', line)
        operand = ast.VariableExpr.DEFAULT
        if context.operand:
            operand = self.visitCall_expr(context.operand)
        argument = self.visit_argument(context)
        if not argument:
            return self.visit_property_call(identifier, operand, line)
        return self.visit_method_call(identifier, operand, argument, line)

    def visit_property_call(self, identifier, operand, line):
        if identifier == ExprConstants.NEXT_SIBLING:
            return ast.NextSiblingExpr(operand, line)
        if identifier == ExprConstants.PREVIOUS_SIBLING:
            return ast.PreviousSiblingExpr(operand, line)
        if identifier == ExprConstants.IS_VENDOR_SPECIFIC:
            return ast.IsVendorSpecificPropertyExpr(operand, line)
        if identifier == ExprConstants.IS_SINGLE_LINE:
            return ast.IsSingleLinePropertyExpr(operand, line)
        if identifier == ExprConstants.IS_KEY:
            return ast.IsKeyPropertyExpr(operand, line)
        if identifier == ExprConstants.UNIT:
            return ast.UnitPropertyExpr(operand, line)
        if identifier == ExprConstants.OPACITY:
            return ast.OpacityPropertyExpr(operand, line)
        if identifier == ExprConstants.STRING:
            return ast.StringPropertyExpr(operand, line)
        if identifier == ExprConstants.VALUE:
            return ast.ValuePropertyExpr(operand, line)
        if identifier == ExprConstants.NUM_VALUE:
            return ast.NumValuePropertyExpr(operand, line)
        if identifier == ExprConstants.PROPERTY:
            return ast.PropertyPropertyExpr(operand, line)
        if identifier == ExprConstants.NAME:
            return ast.NamePropertyExpr(operand, line)
        if identifier == ExprConstants.IS_LONG:
            return ast.IsLongPropertyExpr(operand, line)
        if identifier == ExprConstants.HAS_SINGLE_QUOTES:
            return ast.HasSingleQuotesPropertyExpr(operand, line)
        if identifier == ExprConstants.HAS_DOUBLE_QUOTES:
            return ast.HasDoubleQuotesPropertyExpr(operand, line)
        if identifier == ExprConstants.STANDARD:
            return ast.StandardPropertyExpr(operand, line)
        if identifier == ExprConstants.ARGUMENT:
            return ast.ArgumentExpr(operand, line)
        return ast.InvalidPropertyExpr(operand, identifier, line)

    def visit_method_call(self, identifier, operand, argument, line):
        if identifier == ExprConstants.CONTAINS_ALL:
            return ast.ContainsAllExpr(operand, argument, line)
        if identifier == ExprConstants.CONTAINS_ANY:
            return ast.ContainsAnyExpr(operand, argument, line)
        if identifier == ExprConstants.CONTAINS:
            return ast.ContainsExpr(operand, argument, line)
        if identifier == ExprConstants.COUNT:
            return ast.CountExpr(operand, argument, line)
        if identifier == ExprConstants.CHILD:
            return ast.ChildMethodExpr(operand, argument, line)
        return ast.InvalidMethodExpr(operand, identifier, argument, line)

    def visit_argument(self, context):
        if context.argument:
            return self.visitBasic_expr(context.argument)
        if context.abstract:
            return self.visitSemantic_node(context.abstract)
        return None

    def visitBasic_expr(self, context):
        if context.primary:
            return self.visitElement(context.primary)
        operator = context.operator.text
        line = context.operator.line
        if operator == '-':
            operand = self.visitArithmetic_expr(context.operand)
            return ast.UnaryMinusExpr(operand, line)
        if operator == '+':
            operand = self.visitArithmetic_expr(context.operand)
            return ast.UnaryPlusExpr(operand)

    def visitList_(self, ctx):
        result = []
        for child in ctx.children:
            if type(child) is Parser.cocoParser.List_elementContext:
                element = self.visitList_element(child)
                result.append(element)
        return ast.ListExpr(result)

    def visitList_element(self, ctx):
        if ctx.element_dec:
            return ast.DecimalExpr(float(ctx.element_dec.text))
        if ctx.element_int:
            return ast.IntegerExpr(int(ctx.element_int.text))
        if ctx.element_str:
            return ast.StringExpr(self.unescape_quotes(ctx.element_str.text))
        if ctx.element_desc:
            return self.visitSemantic_node(ctx.element_desc)
        raise ValueError('Unknown list element')

    def visitNode_type(self, ctx):
        if ctx.parenthesis:
            return self.visitNode_type(ctx.parenthesis)
        if ctx.operand:
            operand = self.visitNode_type(ctx.operand)
            return ast.NotExpr(operand)
        if ctx.left:
            left = self.visitNode_type(ctx.left)
            right = self.visitNode_type(ctx.right)
            if ctx.operator.text == 'and':
                return ast.AndExpr(left, right)
            if ctx.operator.text == 'or':
                return ast.OrExpr(left, right)
        if ctx.primary:
            return ast.NodeTypeExpr(ctx.primary.text)
        raise ValueError('Unknown type expression')

    def get_node_descriptor(self, ctx):
        if ctx.primary:
            return ast.NodeTypeDescriptor(type_=ctx.primary.text)
        lambda_string = self.get_type_expression_string(ctx)
        lambda_ = eval('lambda n: ' + lambda_string)
        return ast.NodeTypeDescriptor(func=lambda_)

    def get_ws_node_descriptor(self, text):
        return ast.NodeTypeDescriptor(type_=text)

    def get_type_expression_string(self, ctx):
        if ctx.parenthesis:
            return self.get_type_expression_string(ctx.children[1])
        if ctx.left:
            left = self.get_type_expression_string(ctx.left)
            right = self.get_type_expression_string(ctx.right)
            return ''.join([left, ' ', ctx.operator.text, ' ', right])
        if ctx.primary:
            return ''.join(['n.matches(\'', ctx.primary.text, '\')'])
        if ctx.operand:
            return 'not (' + self.get_type_expression_string(ctx.operand) + ')'
        raise ValueError('Unknown type expression')

    def unescape_quotes(self, string):
        if len(string) < 2:
            return string
        result = string[1:-1]
        return result.replace('\\\'', '\'')