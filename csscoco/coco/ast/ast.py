

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
        return [SequencePatternExpr([NodeExprWrapper(NodeDescriptor('newline')),
                                     NodeSequenceExprWrapper(NodeDescriptor('indent'), Repeater(1, 1)),
                                     NodeExprWrapper(NodeDescriptor('comment'))]),
                SequencePatternExpr.build_simple_seq('newline', 'comment'),
                SequencePatternExpr.build_simple_seq('indent'),
                SequencePatternExpr.build_simple_seq('comment')
                ]

    def get_ignored_and_target_patterns(self):
        # return []
        return self.get_ignored_patterns() + \
            [SequencePatternExpr.build_simple_seq('space'),
             SequencePatternExpr.build_simple_seq('newline'),
             SequencePatternExpr.build_simple_seq('tab')]


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

        # def get_target_patterns(self):
        # return self.get_ignored_patterns()
        #            # [seqs.Sequence([descriptors.NegativeSimpleDescriptor(type_='comment')])]
        #
        # def get_ignored_patterns(self):
        #     return [seqs.SiblingSequence([descriptors.NodeDescriptor.INDENT])]
        #
        # def is_marker_in_condition(self, marker):
        #     return True
        # return type(marker) is not markers.CommentMarker


class SemanticContext(Context):
    def __init__(self, conventions, exceptions):
        super(SemanticContext, self).__init__(conventions, exceptions)

    # TODO: filters must be separated and applied sequentially: first the indent, then everything else
    def get_ignored_patterns(self):
        return [
            SequencePatternExpr.build_simple_seq('space'),
            SequencePatternExpr.build_simple_seq('newline'),
            SequencePatternExpr.build_simple_seq('comment'),
            SequencePatternExpr.build_simple_seq('indent'),
            SequencePatternExpr.build_simple_seq('tab'),
        ]

    def get_ignored_and_target_patterns(self):
        return self.get_ignored_patterns() + \
            []


class Statement(AstNode):
    pass


class Convention(Statement):
    def __init__(self, target_pattern, message):
        self.target_pattern = target_pattern
        self.message = message


class FindRequireConvention(Convention):
    def __init__(self, target_pattern, message, constraint):
        super(FindRequireConvention, self).__init__(target_pattern, message)
        self.constraint = constraint


class ForbidConvention(Convention):
    def __init__(self, target_pattern, message):
        super(ForbidConvention, self).__init__(target_pattern, message)


class FindForbidConvention(Convention):
    def __init__(self, target_pattern, message, constraint):
        super(FindForbidConvention, self).__init__(target_pattern, message)
        self.constraint = constraint


class PatternExpr(AstNode):
    def __init__(self, root_node, all_nodes, relations):
        self.root_desc = root_node
        self.all_descs = all_nodes
        self.relations = relations

    def get_node_relations(self, node_desc):
        return self.relations.get_relations(node_desc)

    def get_anchors(self):
        if self.relations.is_empty():
            return [self.root_desc]
        return self.relations.get_anchors()


class HierarchicalPatternExpr(PatternExpr):
    def __init__(self, root_desc, all_desc, relations):
        super(HierarchicalPatternExpr, self).__init__(root_desc, all_desc, relations)


class SequencePatternExpr(PatternExpr):
    """
    A Sequence is a specific type of pattern with nodes that are only adjacent siblings
    """
    # TODO: Sequences should be able to describe an arbitrary number of repeating node, e.g. newline{2,}
    def __init__(self, node_desc_list):
        """
        The descriptors are of type NodeExprBase, they can be regular NodeWrappers or WeirdGreedyCreatures
        """
        super(SequencePatternExpr, self).__init__(node_desc_list[0],
                                                  node_desc_list,
                                                  Relations.build_sequence_relations(node_desc_list))

    @staticmethod
    def build_simple_seq(*node_type_expr):
        res = []
        for node_type in node_type_expr:
            # is_expr = IsExpr(ImplicitVariableExpr.DEFAULT, node_type)
            res.append(NodeExprWrapper(NodeDescriptor.build_type(node_type)))
        return SequencePatternExpr(res)


class WhitespaceVariation(AstNode):
    """
    Contains all available sequences, e.g.
    (a space b) or (a space newline b)
    """
    def __init__(self, sequences):
        self.sequences = sequences


class Relations(object):
    def __init__(self):
        self.inner = {}

    @staticmethod
    def build_sequence_relations(node_desc_list):
        result = Relations()
        for i in range(0, len(node_desc_list) - 1):
            rel = IsPreviousSiblingOfRelation(node_desc_list[i + 1])
            result.register_relation(node_desc_list[i], rel)
        return result

    def is_empty(self):
        return len(self.inner) == 0

    def register_relation(self, source_node_desc, r):
        if source_node_desc not in self.inner:
            self.inner[source_node_desc] = []
        self.inner[source_node_desc].append(r)

    def get_relations(self, node_desc):
        return self.inner[node_desc] if node_desc in self.inner else []

    def get_anchors(self):
        anchors = []
        for key in self.inner:
            relatives = self.inner[key]
            for r in relatives:
                if r.target_node not in self.inner:
                    anchors.append(r.target_node)
        return anchors

Relations.EMPTY = Relations()


class NodeRelation(object):
    def __init__(self, target_node):
        self.target_node = target_node


class VerticalRelation(NodeRelation):
    def __init__(self, target_node):
        super(VerticalRelation, self).__init__(target_node)


class IsParentOfRelation(VerticalRelation):
    def __init__(self, target_node):
        super(IsParentOfRelation, self).__init__(target_node)


class IsAncestorOfRelation(VerticalRelation):
    def __init__(self, target_node):
        super(IsAncestorOfRelation, self).__init__(target_node)


class HorizontalRelation(NodeRelation):
    def __init__(self, target_node):
        super(HorizontalRelation, self).__init__(target_node)


class IsPreviousSiblingOfRelation(HorizontalRelation):
    def __init__(self, target_node):
        super(IsPreviousSiblingOfRelation, self).__init__(target_node)


class IsNextSiblingOfRelation(HorizontalRelation):
    def __init__(self, target_node):
        super(IsNextSiblingOfRelation, self).__init__(target_node)


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


class NodeExprBase(AstNode):
    def __init__(self, type_desc):
        self.type_desc = type_desc

    def has_add_constraints(self):
        return False


class NodeSequenceExprWrapper(NodeExprBase):
    def __init__(self, type_desc, repeater):
        super(NodeSequenceExprWrapper, self).__init__(type_desc)
        self.repeater = repeater


class NodeExprWrapper(NodeExprBase):
    def __init__(self, type_desc, attr_expr=None):
        super(NodeExprWrapper, self).__init__(type_desc)
        self.attr_expr = attr_expr

    def has_add_constraints(self):
        return self.attr_expr is not None

    def has_identifier(self):
        return False


class NodeExprWrapperWithId(NodeExprWrapper):
    def __init__(self, node_type, identifier, attr_expr=None):
        super(NodeExprWrapperWithId, self).__init__(node_type, attr_expr=attr_expr)
        self.identifier = identifier

    def has_identifier(self):
        return True


class Expr(AstNode):
    pass


class LiteralExpr(Expr):
    def __init__(self, value):
        self.value = value


class DecimalExpr(LiteralExpr):
    def __init__(self, value):
        super(DecimalExpr, self).__init__(value)


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
    def __init__(self, variable_name):
        self.variable_name = variable_name

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


class EqualsExpr(BinaryExpr):
    def __init__(self, left, right):
        super(EqualsExpr, self).__init__(left, right)


class NotEqualsExpr(BinaryExpr):
    def __init__(self, left, right):
        super(NotEqualsExpr, self).__init__(left, right)


class GreaterThanExpr(BinaryExpr):
    def __init__(self, left, right):
        super(GreaterThanExpr, self).__init__(left, right)


class GreaterThanOrEqExpr(BinaryExpr):
    def __init__(self, left, right):
        super(GreaterThanOrEqExpr, self).__init__(left, right)


class LessThanExpr(BinaryExpr):
    def __init__(self, left, right):
        super(LessThanExpr, self).__init__(left, right)


class LessThanOrEqExpr(BinaryExpr):
    def __init__(self, left, right):
        super(LessThanOrEqExpr, self).__init__(left, right)


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
