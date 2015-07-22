import csscoco.lang.visitor_decorator as vis
import csscoco.lang.ast.ast as ast


class TypeChecker(object):
    """
    The class checks for types conformance. Specifically it checks for the following:
    0. List has the same type elements
    1. Unary operator accepts integers
    2. Repeater is correct
    3. Or And and Not have boolean operands
    4. Eq and NotEq have operands of the same type
    5. other comparison operators have integers
    6. Is has node and node type
    7. Match has a string and a string
    8. In has a list of values
    9. Call invokes stuff that is there
    10. NodeQuery has a node
    11. Contains and ContainsAll ?
    12. Before After Between have a Whitespace variation and nodes
    13. Whether identifiers in the constraint are defined
    """
    def __init__(self):
        self._context = TypeCheckingContext()
        self._errors = Errors(self._context)

    @staticmethod
    def check(coco_ast):
        checker = TypeChecker()
        return checker._visit(coco_ast)

    @vis.visitor(ast.ConventionSet)
    def _visit(self, conv_set):
        for context in conv_set.contexts:
            self._context.set_current_context(context)
            self._visit(context)
        return self._errors

    @vis.visitor(ast.Context)
    def _visit(self, context):
        for convention in context.conventions:
            self._context.set_current_convention(convention)
            self._visit(convention)

    @vis.visitor(ast.Convention)
    def _visit(self, convention):
        self._visit(convention.pattern)
        if convention.has_constraint():
            self._visit(convention.constraint)

    @vis.visitor(ast.PatternDescriptor)
    def _visit(self, pattern_desc):
        for node_desc in pattern_desc.nodes:
            self._visit(node_desc)

    @vis.visitor(ast.Node)
    def _visit(self, node):
        if node.has_identifier():
            self._context.register_identifier(node.identifier)
        self._context.set_current_node(node.descriptor)
        if node.has_constraint():
            constraint_type = self._visit(node.constraint)
            if not constraint_type.is_undefined() and not constraint_type.is_boolean():
                self._errors.log(ErrorMessageBuilder.not_boolean_constraint_error(constraint_type, node.line))
                return ast.UndefinedType.TYPE
        return ast.CocoNodeType.TYPE

    @vis.visitor(ast.WhitespaceNode)
    def _visit(self, node):
        if node.repeater.lower < 1 or node.repeater.upper < 1:
            self._errors.log(ErrorMessageBuilder.repeater_with_negative_limit_error(node))
        return ast.CocoNodeType

    @vis.visitor(ast.WhitespaceVariation)
    def _visit(self, variation):
        for seq in variation.sequences:
            self._visit(seq)
        return ast.CocoNodeType.TYPE

    @vis.visitor(ast.UnaryExpr)
    def _visit(self, expr):
        type_operand = self._visit(expr.operand)
        if type_operand.is_undefined():
            return type_operand
        if not expr.is_type_compatible(type_operand):
            self._errors.log(ErrorMessageBuilder.build_unary_type_error(expr, type_operand))
            return ast.UndefinedType.TYPE
        return expr.get_return_type()

    @vis.visitor(ast.BinaryExpr)
    def _visit(self, expr):
        type_left = self._visit(expr.left)
        type_right = self._visit(expr.right)
        if type_left.is_undefined() or type_right.is_undefined():
            return ast.UndefinedType.TYPE
        if not expr.are_types_compatible(type_left, type_right):
            self._errors.log(ErrorMessageBuilder.build_binary_type_error(expr, type_left, type_right))
            return ast.UndefinedType.TYPE
        return expr.get_return_type()

    @vis.visitor(ast.PropertyExpr)
    def _visit(self, expr):
        operand_type = self._visit(expr.operand)
        if operand_type.is_undefined():
            return operand_type
        # TODO: Add a check whether the invoked property is defined for the specific CssNode
        # Consider the following example. Has-single-quotes cannot be checked
        # statically because at runtime the type is narrowed:
        # find v=attribute-value require v is string and v.has-single-quotes

        return expr.get_return_type()

    @vis.visitor(ast.InvalidPropertyExpr)
    def _visit(self, expr):
        error_msg = ErrorMessageBuilder.unknown_call_error(expr)
        self._errors.log(error_msg)
        return ast.UndefinedType.TYPE

    @vis.visitor(ast.InvalidMethodExpr)
    def _visit(self, expr):
        error_msg = ErrorMessageBuilder.unknown_call_error(expr)
        self._errors.log(error_msg)
        return ast.UndefinedType.TYPE

    @vis.visitor(ast.NodeQueryExpr)
    def _visit(self, expr):
        return expr.get_return_type()

    @vis.visitor(ast.NodeQueryWithArgExpr)
    def _visit(self, expr):
        arg_type = self._visit(expr.argument)
        if arg_type.is_undefined():
            return ast.UndefinedType.TYPE
        if not expr.is_type_compatible(arg_type):
            self._errors.log(ErrorMessageBuilder.invalid_argument_error(expr, arg_type))
            return ast.UndefinedType.TYPE
        return expr.get_return_type()

    @vis.visitor(ast.VariableExpr)
    def _visit(self, expr):
        if expr.name != '' and not self._context.is_identifier_registered(expr.name):
            self._errors.log(ErrorMessageBuilder.unregistered_id_error(expr))
            return ast.UndefinedType.TYPE
        return ast.CssNodeType.TYPE

    @vis.visitor(ast.StringExpr)
    def _visit(self, expr):
        return ast.StringType.TYPE

    @vis.visitor(ast.BooleanExpr)
    def _visit(self, expr):
        return ast.BooleanType.TYPE

    @vis.visitor(ast.IntegerExpr)
    def _visit(self, expr):
        return ast.IntegerType.TYPE

    @vis.visitor(ast.ListExpr)
    def _visit(self, expr):
        if not expr.value:
            return ast.ListType('')
        first_type = self._visit(expr.value[0])
        for el in expr.value:
            next_type = self._visit(el)
            if first_type != next_type:
                self._errors.log(ErrorMessageBuilder.heterogeneos_list_error(first_type, next_type, expr.line))
                return ast.UndefinedType.TYPE
        return ast.ListType(first_type)


    @vis.visitor(ast.NodeTypeExpr)
    def _visit(self, expr):
        return ast.CssNodeTypeType.TYPE

    @vis.visitor(ast.NodeQueryExpr)
    def _visit(self, expr):
        return ast.UndefinedType.TYPE


class Errors(object):
    def __init__(self, context):
        self._context = context
        self._inner = {}

    def log(self, error_msg):
        conv = self._context.get_current_convention()
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
        self._context = None
        self._convention = None
        self._node_type = None
        self._id_table = set()

    def set_current_context(self, context):
        self._context = context

    def set_current_convention(self, convention):
        self._convention = convention
        self._id_table = set()

    def set_current_node(self, node_type):
        self._node_type = node_type

    def get_current_convention(self):
        return self._convention

    def get_current_node(self):
        return self._node_type

    def register_identifier(self, i):
        self._id_table.add(i)

    def is_identifier_registered(self, i):
        return i in self._id_table


class ErrorMessageBuilder(object):

    @staticmethod
    def build_binary_type_error(expr, type_left, type_right):
        e = expr.__class__.__name__
        l = type_left.__class__.__name__[:-4]
        r = type_right.__class__.__name__[:-4]
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - Expression of type ', e,
                        ' is not allowed to have arguments of types: ', l, ' and ', r, '.'])

    @staticmethod
    def build_unary_type_error(expr, type_operand):
        e = expr.__class__.__name__
        o = type_operand.__class__.__name__[:-4]
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - Expression of type ', e,
                        ' is not allowed to have argument of type: ', o, '.'])

    @staticmethod
    def not_boolean_constraint_error(type_operand, line):
        t = type_operand.__class__.__name__[:-4]
        line = str(line)
        return ''.join(['Error on line ', line, ' - The constraint of node is of type : ',
                        t, ' and it should be boolean instead.'])

    @staticmethod
    def unknown_call_error(expr):
        e = expr.value
        line = str(expr.line)
        return ''.join(['Error on line ', line, ' - There is not a property/method with name: ', e, '.'])

    @staticmethod
    def heterogeneos_list_error(first_type, second_type, line):
        f = first_type.__class__.__name__[:-4]
        s = second_type.__class__.__name__[:-4]
        line = str(line)
        return ''.join(['Error on line ', line, ' - List contains elements of different types: ', f, ' and ', s, '.'])

    @staticmethod
    def invalid_argument_error(expr, arg_type):
        e = expr.__class__.__name__
        a = arg_type.__class__.__name__[:-4]
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