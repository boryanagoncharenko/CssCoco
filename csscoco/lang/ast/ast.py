

class AstNode(object):
    pass
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
        self.contexts = contexts


class Context(AstNode):
    def __init__(self, conventions, exceptions):
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
        return [SequencePattern([Node(NodeDescriptor('newline')),
                                     WhitespaceNode(NodeDescriptor('indent'), Repeater(1, 1)),
                                     Node(NodeDescriptor('comment'))]),
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
        self.pattern = pattern
        self.description = description


class ForbidConvention(Convention):
    def __init__(self, pattern, description):
        super(ForbidConvention, self).__init__(pattern, description)


class FindConvention(Convention):
    def __init__(self, pattern, description, constraint):
        super(FindConvention, self).__init__(pattern, description)
        self.constraint = constraint


class FindRequireConvention(FindConvention):
    def __init__(self, pattern, description, constraint):
        super(FindRequireConvention, self).__init__(pattern, description, constraint)


class FindForbidConvention(FindConvention):
    def __init__(self, pattern, description, constraint):
        super(FindForbidConvention, self).__init__(pattern, description, constraint)


class Pattern(AstNode):
    def __init__(self, root, nodes, relations):
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


class SequencePattern(Pattern):
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
            res.append(Node(NodeDescriptor.build_type(node_type)))
        return SequencePattern(res)


class WhitespaceVariation(AstNode):
    """
    Contains all available sequences, e.g.
    (a space b) or (a space newline b)
    """
    def __init__(self, sequences):
        self.sequences = sequences


class NodeRelation(AstNode):
    def __init__(self, target_node):
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


class NodeBase(AstNode):
    def __init__(self, descriptor):
        self.descriptor = descriptor

    def has_constraints(self):
        pass

    def has_identifier(self):
        pass


class WhitespaceNode(NodeBase):
    def __init__(self, descriptor, repeater):
        super(WhitespaceNode, self).__init__(descriptor)
        self.repeater = repeater

    def has_constraints(self):
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


class Node(NodeBase):
    # TODO: should this be NodeExpr?
    def __init__(self, descriptor, constraint=None, identifier=None):
        super(Node, self).__init__(descriptor)
        self.constraint = constraint
        self.identifier = identifier

    def has_constraints(self):
        return self.constraint is not None

    def has_identifier(self):
        return self.identifier is not None


class Expr(AstNode):
    pass


class LiteralExpr(Expr):
    def __init__(self, value):
        self.value = value


class IntegerExpr(LiteralExpr):
    def __init__(self, value):
        super(IntegerExpr, self).__init__(value)


class StringExpr(LiteralExpr):
    def __init__(self, value):
        super(StringExpr, self).__init__(value)


class BooleanExpr(LiteralExpr):
    def __init__(self, value):
        super(BooleanExpr, self).__init__(value)

    @staticmethod
    def build(bool_value):
        return BooleanExpr.TRUE if bool_value else BooleanExpr.FALSE

BooleanExpr.TRUE = BooleanExpr(True)
BooleanExpr.FALSE = BooleanExpr(False)


class ListExpr(LiteralExpr):
    def __init__(self, value):
        super(ListExpr, self).__init__(value)


class NodeTypeExpr(LiteralExpr):
    def __init__(self, value):
        super(NodeTypeExpr, self).__init__(value)


class VariableExpr(Expr):
    def __init__(self, name):
        self.name = name

VariableExpr.DEFAULT = VariableExpr('')


class UnaryExpr(Expr):
    def __init__(self, operand):
        self.operand = operand


class NotExpr(UnaryExpr):
    def __init__(self, operand):
        super(NotExpr, self).__init__(operand)


class UnaryMinusExpr(UnaryExpr):
    def __init__(self, operand):
        super(UnaryMinusExpr, self).__init__(operand)


class BinaryExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class OrExpr(BinaryExpr):
    def __init__(self, left, right):
        super(OrExpr, self).__init__(left, right)


class AndExpr(BinaryExpr):
    def __init__(self, left, right):
        super(AndExpr, self).__init__(left, right)


class EqualExpr(BinaryExpr):
    def __init__(self, left, right):
        super(EqualExpr, self).__init__(left, right)


class NotEqualExpr(BinaryExpr):
    def __init__(self, left, right):
        super(NotEqualExpr, self).__init__(left, right)


class GreaterThanExpr(BinaryExpr):
    def __init__(self, left, right):
        super(GreaterThanExpr, self).__init__(left, right)


class GreaterThanOrEqualExpr(BinaryExpr):
    def __init__(self, left, right):
        super(GreaterThanOrEqualExpr, self).__init__(left, right)


class LessThanExpr(BinaryExpr):
    def __init__(self, left, right):
        super(LessThanExpr, self).__init__(left, right)


class LessThanOrEqualExpr(BinaryExpr):
    def __init__(self, left, right):
        super(LessThanOrEqualExpr, self).__init__(left, right)


class IsExpr(BinaryExpr):
    def __init__(self, left, right):
        super(IsExpr, self).__init__(left, right)


class MatchExpr(BinaryExpr):
    def __init__(self, left, right):
        super(MatchExpr, self).__init__(left, right)


class InExpr(BinaryExpr):
    def __init__(self, left, right):
        super(InExpr, self).__init__(left, right)


class CallExpr(Expr):
    def __init__(self, operand, value):
        self.operand = operand
        self.value = value


class PropertyExpr(CallExpr):
    def __init__(self, operand, value):
        super(PropertyExpr, self).__init__(operand, value)


class MethodExpr(PropertyExpr):
    def __init__(self, operand, value, argument):
        super(MethodExpr, self).__init__(operand, value)
        self.argument = argument


class NodeQueryExpr(Expr):
    def __init__(self, operand):
        self.operand = operand


class NextSiblingExpr(NodeQueryExpr):
    def __init__(self, operand):
        super(NextSiblingExpr, self).__init__(operand)


class PreviousSiblingExpr(NodeQueryExpr):
    def __init__(self, operand):
        super(PreviousSiblingExpr, self).__init__(operand)


class NodeQueryWithArgExpr(NodeQueryExpr):
    def __init__(self, operand, argument):
        super(NodeQueryWithArgExpr, self).__init__(operand)
        self.argument = argument


class ContainsExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, argument):
        super(ContainsExpr, self).__init__(operand, argument)


class ContainsAllExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, argument):
        super(ContainsAllExpr, self).__init__(operand, argument)


class CountExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, argument):
        super(CountExpr, self).__init__(operand, argument)


class BeforeExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, variation):
        super(BeforeExpr, self).__init__(operand, variation)


class AfterExpr(NodeQueryWithArgExpr):
    def __init__(self, operand, variation):
        super(AfterExpr, self).__init__(operand, variation)


class BetweenExpr(NodeQueryWithArgExpr):
    def __init__(self, left_operand, variation, right_operand):
        super(BetweenExpr, self).__init__(left_operand, variation)
        self.second_operand = right_operand


class NodeDescriptor(AstNode):
    def __init__(self, type_=None, func=None):
        self.type_ = type_
        self.func = func

    @staticmethod
    def build_any():
        return NodeDescriptor()

    @staticmethod
    def build_type(type_):
        return NodeDescriptor(type_=type_)

    @staticmethod
    def build_expr(f):
        return NodeDescriptor(func=f)

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
