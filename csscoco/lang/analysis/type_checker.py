import csscoco.lang.visitor_decorator as vis
import csscoco.lang.ast.ast as ast
import csscoco.lang.ast.types as types


class TypeChecker(object):
    """
    The class ensures that evaluation will not cause an error. Specifically it does the following:
    1. Checks whether all unary and binary operators have operands of the allowed types
    2. Checks whether a List has elements of the same type
    3. Checks whether a Repeater has correct lower and upper limits
    4. Checks whether undeclared identifiers are used
    """
    def __init__(self):
        self._type_checking_context = TypeCheckingContext()
        self._errors = Errors(self._type_checking_context)

    @staticmethod
    def check(coco_ast):
        checker = TypeChecker()
        return checker._visit(coco_ast)

    @vis.visitor(ast.ConventionSet)
    def _visit(self, conv_set):
        for context in conv_set.contexts:
            self._type_checking_context.context = context
            self._visit(context)
        return self._errors

    @vis.visitor(ast.Context)
    def _visit(self, context):
        for convention in context.conventions:
            self._type_checking_context.convention = convention
            self._visit(convention)

    @vis.visitor(ast.Convention)
    def _visit(self, convention):
        self._visit(convention.pattern)
        if convention.has_constraint():
            constraint_type = self._visit(convention.constraint)
            if self._is_not_boolean_constraint(constraint_type, convention.constraint.line):
                return types.Error.TYPE

    @vis.visitor(ast.PatternDescriptor)
    def _visit(self, pattern_desc):
        for node_desc in pattern_desc.nodes:
            self._visit(node_desc)

    @vis.visitor(ast.PatternConstraintDescriptor)
    def _visit(self, pattern_desc):
        for node_desc in pattern_desc.nodes:
            self._visit(node_desc)
        constraint_type = self._visit(pattern_desc.constraint)
        if self._is_not_boolean_constraint(constraint_type, pattern_desc.constraint.line):
                return types.Error.TYPE

    def _is_not_boolean_constraint(self, constraint_type, line):
        if not constraint_type.is_error() and not constraint_type.is_boolean():
            self._errors.log(ErrorMessageBuilder.not_boolean_constraint_error(constraint_type, line))
            return True
        return False

    @vis.visitor(ast.Node)
    def _visit(self, node):
        if node.has_identifier():
            self._type_checking_context.identifiers_table.add(node.identifier)
        self._type_checking_context.node_type = node.descriptor
        if node.has_constraint():
            constraint_type = self._visit(node.constraint)
            if self._is_not_boolean_constraint(constraint_type, node.line):
                return types.Error.TYPE
        return types.CocoNode.TYPE

    @vis.visitor(ast.WhitespaceNode)
    def _visit(self, node):
        if node.repeater.lower < 1 and node.repeater.upper < 1:
            self._errors.log(ErrorMessageBuilder.repeater_with_negative_limit_error(node))
        return types.CocoNode.TYPE

    @vis.visitor(ast.WhitespaceVariation)
    def _visit(self, variation):
        for seq in variation.sequences:
            self._visit(seq)
        return types.CocoNode.TYPE

    @vis.visitor(ast.UnaryExpr)
    def _visit(self, expr):
        type_operand = self._visit(expr.operand)
        if type_operand.is_error():
            return type_operand
        if not expr.is_type_compatible(type_operand):
            self._errors.log(ErrorMessageBuilder.build_unary_type_error(expr, type_operand))
            return types.Error.TYPE
        return expr.get_return_type()

    @vis.visitor(ast.BinaryExpr)
    def _visit(self, expr):
        type_left = self._visit(expr.left)
        type_right = self._visit(expr.right)
        if type_left.is_error() or type_right.is_error():
            return types.Error.TYPE
        if not expr.are_types_compatible(type_left, type_right):
            self._errors.log(ErrorMessageBuilder.build_binary_type_error(expr, type_left, type_right))
            return types.Error.TYPE
        return expr.get_return_type()

    @vis.visitor(ast.PropertyExpr)
    def _visit(self, expr):
        operand_type = self._visit(expr.operand)
        if operand_type.is_error():
            return operand_type
        return expr.get_return_type()

    @vis.visitor(ast.InvalidPropertyExpr)
    def _visit(self, expr):
        error_msg = ErrorMessageBuilder.unknown_call_error(expr)
        self._errors.log(error_msg)
        return types.Error.TYPE

    @vis.visitor(ast.InvalidMethodExpr)
    def _visit(self, expr):
        error_msg = ErrorMessageBuilder.unknown_call_error(expr)
        self._errors.log(error_msg)
        return types.Error.TYPE

    @vis.visitor(ast.NodeQueryExpr)
    def _visit(self, expr):
        operand = self._visit(expr.operand)
        if operand.is_error():
            return types.Error.TYPE
        return expr.get_return_type()

    @vis.visitor(ast.NodeQueryWithArgExpr)
    def _visit(self, expr):
        operand = self._visit(expr.operand)
        arg_type = self._visit(expr.argument)
        if operand.is_error() or arg_type.is_error():
            return types.Error.TYPE
        if not expr.is_type_compatible(arg_type):
            self._errors.log(ErrorMessageBuilder.invalid_argument_error(expr, arg_type))
            return types.Error.TYPE
        return expr.get_return_type()

    @vis.visitor(ast.VariableExpr)
    def _visit(self, expr):
        if expr.name != '' and expr.name not in self._type_checking_context.identifiers_table:
            self._errors.log(ErrorMessageBuilder.unregistered_id_error(expr))
            return types.Error.TYPE
        return types.CssNode.TYPE

    @vis.visitor(ast.StringExpr)
    def _visit(self, expr):
        return types.String.TYPE

    @vis.visitor(ast.BooleanExpr)
    def _visit(self, expr):
        return types.Boolean.TYPE

    @vis.visitor(ast.DecimalExpr)
    def _visit(self, expr):
        return types.Decimal.TYPE

    @vis.visitor(ast.IntegerExpr)
    def _visit(self, expr):
        return types.Integer.TYPE

    @vis.visitor(ast.ListExpr)
    def _visit(self, expr):
        if not expr.value:
            return types.List('')
        first_type = self._visit(expr.value[0])
        for el in expr.value:
            next_type = self._visit(el)
            if first_type != next_type:
                self._errors.log(ErrorMessageBuilder.heterogeneos_list_error(first_type, next_type, expr.line))
                return types.Error.TYPE
        return types.List(first_type)


    @vis.visitor(ast.NodeTypeExpr)
    def _visit(self, expr):
        return types.CssNodeType.TYPE


class Errors(object):
    def __init__(self, context):
        self._context = context
        self._inner = {}

    def log(self, error_msg):
        conv = self._context.convention
        if conv in self._inner:
            self._inner[conv].append(error_msg)
        else:
            self._inner[conv] = [error_msg]

    def contain_errors(self):
        return len(self._inner) > 0

    def get_errors_for_convention(self, convention):
        if convention in self._inner:
            return self._inner[convention]
        return []

    def get_errors(self):
        result = []
        for c in self._inner:
            result += self._inner[c]
        return result

    def string(self):
        result = 'Error log:'
        for conv in self._inner:
            for error in self._inner[conv]:
                result = ''.join([result, '\n', error])
        return result


class TypeCheckingContext(object):
    def __init__(self):
        self.context = None
        self.__convention = None
        self.node_type = None
        self.identifiers_table = set()

    @property
    def convention(self):
        return self.__convention

    @convention.setter
    def convention(self, convention):
        self.__convention = convention
        self.identifiers_table = set()


class ErrorMessageBuilder(object):
    @staticmethod
    def build_binary_type_error(expr, type_left, type_right):
        e = expr.__class__.__name__
        l = type_left.__class__.__name__
        r = type_right.__class__.__name__
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - Expression of type ', e,
                        ' is not allowed to have arguments of types: ', l, ' and ', r, '.'])

    @staticmethod
    def build_unary_type_error(expr, type_operand):
        e = expr.__class__.__name__
        o = type_operand.__class__.__name__
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - Expression of type ', e,
                        ' is not allowed to have argument of type: ', o, '.'])

    @staticmethod
    def not_boolean_constraint_error(type_operand, line):
        t = type_operand.__class__.__name__
        line = str(line)
        return ''.join(['Error on line ', line, ' - The constraint is of type \'',
                        t, '\' and it should be boolean instead.'])

    @staticmethod
    def unknown_call_error(expr):
        e = expr.value
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - There is not a property/method with name: ', e, '.'])

    @staticmethod
    def heterogeneos_list_error(first_type, second_type, line):
        f = first_type.__class__.__name__
        s = second_type.__class__.__name__
        line = str(line)
        return ''.join(['Error on line ', line, ' - List contains elements of different types: ', f, ' and ', s, '.'])

    @staticmethod
    def invalid_argument_error(expr, arg_type):
        e = expr.__class__.__name__
        a = arg_type.__class__.__name__
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - Expression of type ', e, ' cannot have argument of type ', a, '.'])

    @staticmethod
    def repeater_with_negative_limit_error(expr):
        e = expr.__class__.__name__
        l = str(e.lower)
        u = str(e.upper)
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - Repeater has a negative limit: lower=', l, ' and upper ', u, '.'])

    @staticmethod
    def unregistered_id_error(expr):
        e = expr.name
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - Undefined variable with name ', e, ' is used.'])