

class AstNode(object):
    def __init__(self, line=-1):
        self.line = line
    # def get_children(self):
    #     return []

    # def get_title(self):
    #     return self.__class__.__name__

    # def pretty_print(self, level=0, print_indent='  '):
    #     s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
    #     for child in self.get_children():
    #         s = ''.join([s, child.pretty_print(level + 1)])
    #     return s


class ConventionSet(AstNode):
    def __init__(self, contexts):
        super(ConventionSet, self).__init__()
        self.contexts = contexts


class Context(AstNode):
    def __init__(self, conventions, exceptions):
        super(Context, self).__init__()
        self.conventions = conventions
        self.exceptions = exceptions

    def get_ignored_and_target_patterns(self):
        """
        What the context targets, i.e. whitespaces, indents, comments
        """
        return []

    def get_ignored_patterns(self):
        """
        What is completely ignored in the context
        """
        return []


class WhitespaceContext(Context):
    def __init__(self, conventions, exceptions):
        super(WhitespaceContext, self).__init__(conventions, exceptions)

    def get_ignored_patterns(self):
        # return []
        return [SequencePattern([Node(NodeTypeDescriptor('newline')),
                                     WhitespaceNode(NodeTypeDescriptor('indent'), Repeater(1, 1)),
                                     Node(NodeTypeDescriptor('comment'))]),
                SequencePattern.build_simple_seq('newline', 'comment'),
                SequencePattern.build_simple_seq('indent'),
                SequencePattern.build_simple_seq('comment')
                ]

    def get_ignored_and_target_patterns(self):
        # return []
        return self.get_ignored_patterns() + \
            [SequencePattern.build_simple_seq('space'),
             SequencePattern.build_simple_seq('newline'),
             SequencePattern.build_simple_seq('tab')]


class IndentContext(Context):
    def __init__(self, conventions, exceptions):
        super(IndentContext, self).__init__(conventions, exceptions)

    def get_ignored_patterns(self):
        return []

    def get_ignored_and_target_patterns(self):
        return []


class CommentsContext(Context):
    def __init__(self, conventions, exceptions):
        super(CommentsContext, self).__init__(conventions, exceptions)


class SemanticContext(Context):
    def __init__(self, conventions, exceptions):
        super(SemanticContext, self).__init__(conventions, exceptions)

    # TODO: filters must be separated and applied sequentially: first the indent, then everything else
    def get_ignored_patterns(self):
        return [
            SequencePattern.build_simple_seq('space'),
            SequencePattern.build_simple_seq('newline'),
            SequencePattern.build_simple_seq('comment'),
            SequencePattern.build_simple_seq('indent'),
            SequencePattern.build_simple_seq('tab'),
        ]

    def get_ignored_and_target_patterns(self):
        return self.get_ignored_patterns() + \
            []


class Convention(AstNode):
    def __init__(self, pattern, description):
        super(Convention, self).__init__()
        self.pattern = pattern
        self.description = description

    def has_constraint(self):
        return False


class ForbidConvention(Convention):
    def __init__(self, pattern, description):
        super(ForbidConvention, self).__init__(pattern, description)


class FindConvention(Convention):
    def __init__(self, pattern, description, constraint):
        super(FindConvention, self).__init__(pattern, description)
        self.constraint = constraint

    def has_constraint(self):
        return True


class FindRequireConvention(FindConvention):
    def __init__(self, pattern, description, constraint):
        super(FindRequireConvention, self).__init__(pattern, description, constraint)


class FindForbidConvention(FindConvention):
    def __init__(self, pattern, description, constraint):
        super(FindForbidConvention, self).__init__(pattern, description, constraint)


class PatternDescriptor(AstNode):
    def __init__(self, root, nodes, relations):
        super(PatternDescriptor, self).__init__()
        self.root = root
        self.nodes = nodes
        self.relations = relations

    def get_node_relations(self, node_desc):
        return self.relations.get_relations(node_desc)

    def get_anchors(self):
        if self.relations.is_empty():
            return [self.root]
        return self.relations.get_anchors()


class NodeRelations(object):
    def __init__(self):
        self._relations = {}

    @staticmethod
    def build_sequence_relations(node_desc_list):
        result = NodeRelations()
        for i in range(0, len(node_desc_list) - 1):
            rel = IsPreviousSiblingOf(node_desc_list[i + 1])
            result.register_relation(node_desc_list[i], rel)
        return result

    def is_empty(self):
        return len(self._relations) == 0

    def register_relation(self, source_node_desc, r):
        if source_node_desc not in self._relations:
            self._relations[source_node_desc] = []
        self._relations[source_node_desc].append(r)

    def get_relations(self, node_desc):
        return self._relations[node_desc] if node_desc in self._relations else []

    def get_anchors(self):
        anchors = []
        for key in self._relations:
            relatives = self._relations[key]
            for r in relatives:
                if r.target_node not in self._relations:
                    anchors.append(r.target_node)
        return anchors

NodeRelations.EMPTY = NodeRelations()


class SequencePattern(PatternDescriptor):
    """
    A Sequence is a specific type of pattern with nodes that are only adjacent siblings
    """
    def __init__(self, node_desc_list):
        """
        The descriptors are of type NodeExprBase, they can be regular NodeWrappers or WeirdGreedyCreatures
        """
        super(SequencePattern, self).__init__(node_desc_list[0],
                                              node_desc_list,
                                              NodeRelations.build_sequence_relations(node_desc_list))

    @staticmethod
    def build_simple_seq(*node_type_expr):
        res = []
        for node_type in node_type_expr:
            # is_expr = IsExpr(ImplicitVariableExpr.DEFAULT, node_type)
            res.append(Node(NodeTypeDescriptor.build_type(node_type)))
        return SequencePattern(res)


class WhitespaceVariation(AstNode):
    """
    Contains all available sequences, e.g.
    (a space b) or (a space newline b)
    """
    def __init__(self, sequences):
        super(WhitespaceVariation, self).__init__()
        self.sequences = sequences


class NodeRelation(AstNode):
    def __init__(self, target_node):
        super(NodeRelation, self).__init__()
        self.target_node = target_node


class IsParentOf(NodeRelation):
    def __init__(self, target_node):
        super(IsParentOf, self).__init__(target_node)


class IsAncestorOf(NodeRelation):
    def __init__(self, target_node):
        super(IsAncestorOf, self).__init__(target_node)


class IsPreviousSiblingOf(NodeRelation):
    def __init__(self, target_node):
        super(IsPreviousSiblingOf, self).__init__(target_node)


class IsNextSiblingOf(NodeRelation):
    def __init__(self, target_node):
        super(IsNextSiblingOf, self).__init__(target_node)


class NodeDescriptor(AstNode):
    def __init__(self, descriptor):
        super(NodeDescriptor, self).__init__()
        self.descriptor = descriptor

    def has_constraints(self):
        pass

    def has_identifier(self):
        pass


class WhitespaceNode(NodeDescriptor):
    def __init__(self, descriptor, repeater):
        super(WhitespaceNode, self).__init__(descriptor)
        self.repeater = repeater

    def has_constraint(self):
        return False

    def has_identifier(self):
        return False


class Repeater(object):
    def __init__(self, lower=1, upper=-1):
        self.lower = lower
        self.upper = upper

    def is_exact(self):
        return self.lower == self.upper

    def is_range(self):
        return self.lower != -1 and self.upper != -1

    def is_max(self):
        return self.lower == -1 and self.upper != -1

    def is_min(self):
        return self.lower != -1 and self.upper == -1

    def is_in_range(self, i):
        assert i >= 0
        if self.is_min():
            return True
        return i < self.upper - self.lower

Repeater.DEFAULT = Repeater()


class Node(NodeDescriptor):
    def __init__(self, descriptor, constraint=None, identifier=None):
        super(Node, self).__init__(descriptor)
        self.constraint = constraint
        self.identifier = identifier

    def has_constraint(self):
        return self.constraint is not None

    def has_identifier(self):
        return self.identifier is not None


class Expr(AstNode):
    def __init__(self, line=-1):
        super(Expr, self).__init__(line=line)


class LiteralExpr(Expr):
    def __init__(self, value, line=-1):
        super(LiteralExpr, self).__init__(line)
        self.value = value


class IntegerExpr(LiteralExpr):
    def __init__(self, value, line=-1):
        super(IntegerExpr, self).__init__(value, line)


class StringExpr(LiteralExpr):
    def __init__(self, value, line=-1):
        super(StringExpr, self).__init__(value, line)


class BooleanExpr(LiteralExpr):
    def __init__(self, value, line=-1):
        super(BooleanExpr, self).__init__(value, line)

    @staticmethod
    def build(bool_value):
        return BooleanExpr.TRUE if bool_value else BooleanExpr.FALSE

BooleanExpr.TRUE = BooleanExpr(True)
BooleanExpr.FALSE = BooleanExpr(False)


class ListExpr(LiteralExpr):
    def __init__(self, value, line=-1):
        super(ListExpr, self).__init__(value, line)


class NodeTypeExpr(LiteralExpr):
    def __init__(self, value, line=-1):
        super(NodeTypeExpr, self).__init__(value, line)


class VariableExpr(Expr):
    def __init__(self, name, line=-1):
        super(VariableExpr, self).__init__(line)
        self.name = name

VariableExpr.DEFAULT = VariableExpr('')


class NaryExpr(Expr):
    pass


class UnaryExpr(NaryExpr):
    def __init__(self, operand, line=-1):
        super(UnaryExpr, self).__init__(line)
        self.operand = operand

    def is_type_compatible(self, t):
        raise NotImplementedError()

    def get_return_type(self):
        raise NotImplementedError()


class NotExpr(UnaryExpr):
    def __init__(self, operand, line=1):
        super(NotExpr, self).__init__(operand, line)

    def is_type_compatible(self, t):
        return t.is_boolean()

    def get_return_type(self):
        return BooleanType.TYPE


class UnaryMinusExpr(UnaryExpr):
    def __init__(self, operand, line=-1):
        super(UnaryMinusExpr, self).__init__(operand, line)

    def is_type_compatible(self, t):
        return t.is_numerical()

    def get_return_type(self):
        return IntegerType.TYPE


class UnaryPlusExpr(UnaryExpr):
    def __init__(self, operand, line=-1):
        super(UnaryPlusExpr, self).__init__(operand, line)

    def is_type_compatible(self, t):
        return t.is_numerical()

    def get_return_type(self):
        return IntegerType.TYPE


class BinaryExpr(NaryExpr):
    def __init__(self, left, right, line=-1):
        super(BinaryExpr, self).__init__(line)
        self.left = left
        self.right = right

    def are_types_compatible(self, left, right):
        raise NotImplementedError()

    def get_return_type(self):
        raise NotImplementedError()


class OrExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(OrExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left.is_boolean() and right.is_boolean()

    def get_return_type(self):
        return BooleanType.TYPE


class AndExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(AndExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left.is_boolean() and right.is_boolean()

    def get_return_type(self):
        return BooleanType.TYPE


class EqualExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(EqualExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left == right

    def get_return_type(self):
        return BooleanType.TYPE


class NotEqualExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(NotEqualExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left == right

    def get_return_type(self):
        return BooleanType.TYPE


class GreaterThanExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(GreaterThanExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left.is_numerical() and right.is_numerical()

    def get_return_type(self):
        return BooleanType.TYPE


class GreaterThanOrEqualExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(GreaterThanOrEqualExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left.is_numerical() and right.is_numerical()

    def get_return_type(self):
        return BooleanType.TYPE


class LessThanExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(LessThanExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left.is_numerical() and right.is_numerical()

    def get_return_type(self):
        return BooleanType.TYPE


class LessThanOrEqualExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(LessThanOrEqualExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left.is_numerical() and right.is_numerical()

    def get_return_type(self):
        return BooleanType.TYPE


class IsExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(IsExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left.is_css_node() and right.is_css_node_type()

    def get_return_type(self):
        return BooleanType.TYPE


class MatchExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(MatchExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return left.is_string() and right.is_string()

    def get_return_type(self):
        return BooleanType.TYPE


class InExpr(BinaryExpr):
    def __init__(self, left, right, line=-1):
        super(InExpr, self).__init__(left, right, line)

    def are_types_compatible(self, left, right):
        return right.is_list()

    def get_return_type(self):
        return BooleanType.TYPE


class CallExpr(Expr):
    def __init__(self, operand, value, line=-1):
        super(CallExpr, self).__init__(line)
        self.operand = operand
        self.value = value

    def get_return_type(self):
        raise NotImplementedError()


class PropertyExpr(CallExpr):
    def __init__(self, operand, value, line=-1):
        super(PropertyExpr, self).__init__(operand, value, line)


class IsVendorSpecificPropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(IsVendorSpecificPropertyExpr, self).__init__(operand, 'is-vendor-specific', line)

    def get_return_type(self):
        return BooleanType.TYPE


class ValuePropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(ValuePropertyExpr, self).__init__(operand, 'value', line)

    def get_return_type(self):
        return CssNodeType.TYPE


class NumValuePropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(NumValuePropertyExpr, self).__init__(operand, 'num-value', line)

    def get_return_type(self):
        return IntegerType.TYPE


class PropertyPropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(PropertyPropertyExpr, self).__init__(operand, 'property', line)

    def get_return_type(self):
        return CssNodeType.TYPE


class NamePropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(NamePropertyExpr, self).__init__(operand, 'name', line)

    def get_return_type(self):
        return StringType.TYPE


class StringPropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(StringPropertyExpr, self).__init__(operand, 'string', line)

    def get_return_type(self):
        return StringType.TYPE


class IsLongPropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(IsLongPropertyExpr, self).__init__(operand, 'is-long', line)

    def get_return_type(self):
        return BooleanType.TYPE


class HasSingleQuotesPropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(HasSingleQuotesPropertyExpr, self).__init__(operand, 'has-single-quotes', line)

    def get_return_type(self):
        return BooleanType.TYPE


class StandardPropertyExpr(PropertyExpr):
    def __init__(self, operand, line=-1):
        super(StandardPropertyExpr, self).__init__(operand, 'standard', line)

    def get_return_type(self):
        return StringType.TYPE


class InvalidPropertyExpr(PropertyExpr):
    def __init__(self, operand, value, line=-1):
        super(InvalidPropertyExpr, self).__init__(operand, value, line)

    def get_return_type(self):
        return UndefinedType.TYPE


class MethodExpr(PropertyExpr):
    def __init__(self, operand, value, argument, line=-1):
        super(MethodExpr, self).__init__(operand, value, line)
        self.argument = argument

    def are_types_valid(self, operand_type, argument_type):
        raise NotImplementedError()

    def get_return_type(self):
        raise NotImplementedError()


class ChildMethodExpr(MethodExpr):
    def __init__(self, operand, argument, line=-1):
        super(ChildMethodExpr, self).__init__(operand, 'child', argument, line)

    def get_return_type(self):
        return CssNodeType.TYPE

    def are_types_valid(self, operand_type, argument_type):
        return operand_type.is_css_node() and argument_type.is_numerical()


class InvalidMethodExpr(MethodExpr):
    def __init__(self, operand, value, argument, line=-1):
        super(InvalidMethodExpr, self).__init__(operand, value, argument, line)

    def get_return_type(self):
        return UndefinedType.TYPE


class NodeQueryExpr(Expr):
    def __init__(self, operand, line=-1):
        super(NodeQueryExpr, self).__init__(line)
        self.operand = operand

    def get_return_type(self):
        raise NotImplementedError()


class NextSiblingExpr(NodeQueryExpr):
    def __init__(self, operand, line=-1):
        super(NextSiblingExpr, self).__init__(operand, line)

    def get_return_type(self):
        return CssNodeType.TYPE


class PreviousSiblingExpr(NodeQueryExpr):
    def __init__(self, operand, line=-1):
        super(PreviousSiblingExpr, self).__init__(operand, line)

    def get_return_type(self):
        return CssNodeType.TYPE


class NodeQueryWithArgExpr(NodeQueryExpr):
    def __init__(self, operand, argument, line=-1):
        super(NodeQueryWithArgExpr, self).__init__(operand, line)
        self.argument = argument

    def is_type_compatible(self, t):
        raise NotImplementedError()

    def get_return_type(self):
        raise NotImplementedError()


class ContainsExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, argument, line=-1):
        super(ContainsExpr, self).__init__(operand, argument, line)

    def is_type_compatible(self, t):
        return t.is_coco_node()

    def get_return_type(self):
        return BooleanType.TYPE


class ContainsAllExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, argument, line=-1):
        super(ContainsAllExpr, self).__init__(operand, argument, line)

    def is_type_compatible(self, t):
        return t.is_list() and t.elements_type.is_coco_node()

    def get_return_type(self):
        return BooleanType.TYPE


class CountExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, argument, line=-1):
        super(CountExpr, self).__init__(operand, argument, line)

    def is_type_compatible(self, t):
        return t.is_coco_node()

    def get_return_type(self):
        return IntegerType.TYPE


class BeforeExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, variation, line=-1):
        super(BeforeExpr, self).__init__(operand, variation, line)

    def is_type_compatible(self, t):
        return t.is_coco_node()

    def get_return_type(self):
        return BooleanType.TYPE


class AfterExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, variation, line=-1):
        super(AfterExpr, self).__init__(operand, variation, line)

    def is_type_compatible(self, t):
        return t.is_coco_node()

    def get_return_type(self):
        return BooleanType.TYPE


class BetweenExpr(NodeQueryWithArgExpr):
    def __init__(self, left_operand, variation, right_operand, line=-1):
        super(BetweenExpr, self).__init__(left_operand, variation, line)
        self.second_operand = right_operand

    def is_type_compatible(self, t):
        return t.is_coco_node()

    def get_return_type(self):
        return BooleanType.TYPE


class NodeTypeDescriptor(AstNode):
    def __init__(self, type_=None, func=None):
        super(NodeTypeDescriptor, self).__init__()
        self.type_ = type_
        self.func = func

    @staticmethod
    def build_any():
        return NodeTypeDescriptor()

    @staticmethod
    def build_type(type_):
        return NodeTypeDescriptor(type_=type_)

    @staticmethod
    def build_expr(f):
        return NodeTypeDescriptor(func=f)

    def is_any(self):
        return not self.type_ and not self.func

    def is_type(self):
        return self.type_ and not self.func

    def is_func(self):
        return not self.type_ and self.func

    def is_node_match(self, node):
        if self.is_any():
            return True
        if self.is_type():
            return self.type_ in node.search_labels
        return self.func(node)


class Type(AstNode):
    def is_numerical(self):
        return False

    def is_string(self):
        return False

    def is_boolean(self):
        return False

    def is_list(self):
        return False

    def is_css_node(self):
        return False

    def is_css_node_type(self):
        return False

    def is_coco_node(self):
        return False

    def is_undefined(self):
        return False


class StringType(Type):
    def is_string(self):
        return True


class IntegerType(Type):
    def is_numerical(self):
        return True


class BooleanType(Type):
    def is_boolean(self):
        return True


class CssNodeTypeType(Type):
    def is_css_node_type(self):
        return True


class CssNodeType(Type):
    def is_css_node(self):
        return True


class CocoNodeType(Type):
    def is_coco_node(self):
        return True


class ListType(Type):
    def __init__(self, elements_type):
        super(ListType, self).__init__()
        self.elements_type = elements_type

    def is_list(self):
        return True

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False


class UndefinedType(Type):
    def is_undefined(self):
        return True

StringType.TYPE = StringType()
IntegerType.TYPE = IntegerType()
BooleanType.TYPE = BooleanType()
CssNodeType.TYPE = CssNodeType()
CssNodeTypeType.TYPE = CssNodeTypeType()
CocoNodeType.TYPE = CocoNodeType()
UndefinedType.TYPE = UndefinedType()
