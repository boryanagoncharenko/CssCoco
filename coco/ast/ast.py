import abc
import coco.ast.ast_node as ast
import coco.ast.expressions as expr
import coco.ast.markers as markers


class Sheet(ast.AstNode):
    def __init__(self, contexts):
        self.contexts = contexts


class Context(ast.AstNode):
    def __init__(self, conventions, exceptions):
        self.conventions = conventions
        self.exceptions = exceptions

    def get_target_patterns(self):
        """
        What the context targets, i.e. whitespaces, indents, comments
        """
        pass

    def get_ignored_patterns(self):
        """
        What is completely ignored in the context
        """
        pass


class WhitespaceContext(Context):
    def __init__(self, conventions, exceptions):
        super(WhitespaceContext, self).__init__(conventions, exceptions)

        # def get_target_patterns(self):
        # return self.get_ignored_patterns() + [seqs.SiblingSequence([descriptors.NodeDescriptor.WHITESPACE])]
        #
        # def get_ignored_patterns(self):
        #     return [seqs.SiblingSequence([descriptors.NodeDescriptor.INDENT]),
        #             seqs.SiblingSequence([descriptors.NodeDescriptor.COMMENT]),
        #             seqs.SiblingSequence([descriptors.SimpleDescriptor(type_='newline'),
        #                            descriptors.SimpleDescriptor(type_='comment')])]

        # def is_marker_in_condition(self, marker):
        #     return marker.is_css_marker()


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
        return [SequencePatternExpr([NodeExprWrapper(IsExpr(ImplicitVariableExpr.DEFAULT, NodeTypeExpr(type_string='newline'))),
                                     NodeSequenceExprWrapper(IsExpr(ImplicitVariableExpr.DEFAULT, NodeTypeExpr(type_string='indent')),Repeater(1, 1)),
                                     NodeExprWrapper(IsExpr(ImplicitVariableExpr.DEFAULT, NodeTypeExpr(type_string='comment')))]),
                SequencePatternExpr.build_simple_seq(NodeTypeExpr(type_string='newline'), NodeTypeExpr(type_string='comment')),
                SequencePatternExpr.build_simple_seq(NodeTypeExpr(type_string='indent')),
                SequencePatternExpr.build_simple_seq(NodeTypeExpr(type_string='comment'))]

    def get_ignored_and_target_patterns(self):
        return self.get_ignored_patterns() + \
            [SequencePatternExpr.build_simple_seq(NodeTypeExpr(type_string='space')),
             SequencePatternExpr.build_simple_seq(NodeTypeExpr(type_string='newline')),
             SequencePatternExpr.build_simple_seq(NodeTypeExpr(type_string='tab'))]


class Statement(ast.AstNode):
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


class PatternExpr(ast.AstNode):
    def __init__(self, root_node, all_nodes, relations):
        self.root_desc = root_node
        self.all_descs = all_nodes
        self.relations = relations

    def get_node_relations(self, node_desc):
        return self.relations.get_relations(node_desc)

    def get_anchors(self):
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
            is_expr = IsExpr(ImplicitVariableExpr.DEFAULT, node_type)
            res.append(NodeExprWrapper(is_expr))
        return SequencePatternExpr(res)


class WhitespaceVariation(ast.AstNode):
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


class NodeExprBase(ast.AstNode):
    def __init__(self, attr_expr):
        self.attr_expr = attr_expr


class NodeSequenceExprWrapper(NodeExprBase):
    def __init__(self, attr_expr, repeater):
        super(NodeSequenceExprWrapper, self).__init__(attr_expr)
        self.repeater = repeater


class NodeExprWrapper(NodeExprBase):
    def __init__(self, attr_expr, identifier=None):
        super(NodeExprWrapper, self).__init__(attr_expr)
        self.identifier = identifier

    def has_identifier(self):
        return self.identifier is not None


class Expr(ast.AstNode):
    pass


class UnaryExpr(Expr):
    def __init__(self, operand):
        self.operand = operand


class NotExpr(UnaryExpr):
    def __init__(self, operand):
        super(NotExpr, self).__init__(operand)


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


class GreaterThanExpr(BinaryExpr):
    def __init__(self, left, right):
        super(GreaterThanExpr).__init__(left, right)


class ConstantExpr(Expr):
    pass


class VariableExpr(ConstantExpr):
    def __init__(self, value):
        self.value_string = value


class ImplicitVariableExpr(VariableExpr):
    def __init__(self):
        super(ImplicitVariableExpr, self).__init__('implicit')


ImplicitVariableExpr.DEFAULT = ImplicitVariableExpr()


class IntegerExpr(ConstantExpr):
    def __init__(self, value):
        self.value = value


class StringExpr(ConstantExpr):
    def __init__(self, value):
        self.value = value


class BooleanExpr(ConstantExpr):
    def __init__(self, value):
        self.value = value

    @staticmethod
    def build(bool_value):
        return BooleanExpr.TRUE if bool_value else BooleanExpr.FALSE


BooleanExpr.TRUE = BooleanExpr(True)
BooleanExpr.FALSE = BooleanExpr(False)


class NodeTypeExpr(ConstantExpr):
    def __init__(self, type_string=None, value_string=None):
        self.type = type_string
        self.value = value_string


class ListExpr(ConstantExpr):
    def __init__(self, value):
        self.value = value


# Type match is a nothing else but an expression about type
# No need for special Or, Not expressions, they are the same as attr


class IsExpr(BinaryExpr):
    def __init__(self, left, right):
        super(IsExpr, self).__init__(left, right)


class ApiCallExpr(Expr):
    def __init__(self, operand, property_string):
        self.operand = operand
        self.property_string = property_string


class ApiCallExprWithArg(ApiCallExpr):
    def __init__(self, operand, property_string, argument):
        super(ApiCallExprWithArg, self).__init__(operand, property_string)
        self.argument = argument


class NodeQueryExpr(Expr):
    def __init__(self, operand):
        self.operand = operand


class ContainsExpr(NodeQueryExpr):
    def __init__(self, operand, argument):
        super(ContainsExpr, self).__init__(operand)
        self.argument = argument


class CountExpr(NodeQueryExpr):
    def __init__(self, operand, argument):
        super(CountExpr, self).__init__(operand)
        self.argument = argument


class NextSiblingExpr(NodeQueryExpr):
    def __init__(self, operand):
        super(NextSiblingExpr, self).__init__(operand)


class WhitespaceExpr(NodeQueryExpr):
    def __init__(self, operand, variation):
        super(WhitespaceExpr, self).__init__(operand)
        self.variation = variation


class BeforeExpr(WhitespaceExpr):
    def __init__(self, operand, variation):
        super(BeforeExpr, self).__init__(operand, variation)


class BetweenExpr(WhitespaceExpr):
    def __init__(self, operand, variation, second_operand):
        super(BetweenExpr, self).__init__(operand, variation)
        self.second_operand = second_operand


class AfterExpr(WhitespaceExpr):
    def __init__(self, operand, variation):
        super(AfterExpr, self).__init__(operand, variation)


class Repetition(Statement):
    def __init__(self, repeat_list, convention):
        self.repeat_list = repeat_list
        self.convention = convention


# -------------- OLD STUFF --------------


class Rule(Statement):
    def __init__(self, markers_list):
        self.markers_list = markers_list

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent * level, self.get_title(), ':'])
        for m in self.markers_list:
            s = ''.join([s, m.pretty_print(level + 1)])
        return s


# for word=(id-word or class-word)
# require word.value in dictionary


class RequireRule(Rule):
    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class ForbidRule(Rule):
    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class AllowRule(Rule):
    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class MarkerSequence(ast.AstNode):
    def __init__(self, markers):
        self.markers = markers

    def __getitem__(self, x):
        return self.markers[x]

    def __iter__(self):
        return iter(self.markers)

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent * level, self.get_title(), ':'])
        for m in self.markers:
            s = ''.join([s, m.pretty_print(level + 1)])
        return s


class MarkerSequenceVariation(ast.AstNode):
    def __init__(self, marker_sequences):
        self.marker_sequences = marker_sequences

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent * level, self.get_title(), ':'])
        for sequence in self.marker_sequences:
            s = ''.join([s, sequence.pretty_print(level + 1)])
        return s


MarkerSequenceVariation.NONE = MarkerSequenceVariation([])


class AstBuilder(object):
    @staticmethod
    def build(ply_tree):
        builder = AstBuilder()
        return builder.__build_sheet(ply_tree)

    def __build_sheet(self, ply_sheet):
        contexts = []
        for c in ply_sheet.select('context'):
            contexts.append(self.__build_context(c))
        return Sheet(contexts)

    def __build_context(self, ply_context):
        statements = []
        for stat in ply_context.select('rule'):
            rule = self.__build_rule(stat)
            statements.append(rule)

        name = ply_context.select('context > *')[0].lower()
        if name == 'whitespace':
            return WhitespaceContext(statements)
        if name == 'comments':
            return CommentsContext(statements)

        raise NotImplementedError('Other contexts are not implemented yet')

    def __build_rule(self, ply_rule):
        children = ply_rule.select('rule > *')
        markers = self._build_markers(children[1:])
        name = children[0].lower()

        if name == 'require':
            return RequireRule(markers)

        if name == 'forbid':
            return ForbidRule(markers)

        if name == 'allow':
            return AllowRule(markers)

        raise NotImplementedError('Other rules are not implemented yet')

    def _build_markers(self, marker_list):
        result = []
        for m in marker_list:
            result.append(self._build_marker(m))
        return result

    def _generate_possible_sequences(self, option_list, res):
        if len(option_list) == 0:
            yield MarkerSequence(list(res))
        else:
            first_option = option_list[0]
            for option in first_option:
                res.append(option)
                yield from self._generate_possible_sequences(option_list[1:], res)
                del res[-1]

    def _build_marker(self, ply_node):
        if self._is_or_expr(ply_node):
            return self._handle_or_expr(ply_node)

        if self._is_parenthesis_expr(ply_node):
            return self._handle_parenthesis_expr(ply_node)

        if self._is_terminal_expr(ply_node):
            return self._handle_terminal_expr(ply_node)

        raise NotImplementedError('Unknown marker')

    def _is_or_expr(self, ply_node):
        return len(ply_node.tail) == 3 and \
               ply_node.tail[1] == 'or'

    def _handle_or_expr(self, ply_node):
        left = self._build_marker(ply_node.tail[0])
        right = self._build_marker(ply_node.tail[2])

        option_list = []
        if type(left) is expr.OrExpression:
            option_list = option_list + left.markers_list
        else:
            option_list.append(left)

        if type(right) is expr.OrExpression:
            option_list = option_list + right.markers_list
        else:
            option_list.append(right)

        return expr.OrExpression(option_list)

    def _is_parenthesis_expr(self, ply_node):
        return ply_node.tail[0] == '(' and \
               ply_node.tail[-1] == ')'

    def _handle_parenthesis_expr(self, ply_node):
        elements = ply_node.tail[1:-1]
        markers = []
        if len(elements) == 1:
            result = self._build_marker(elements[0])
            if type(result) in [expr.OrExpression, expr.MarkersExpression]:
                return result

        for element in elements:
            markers.append(self._build_marker_two(element))
        return expr.MarkersExpression(markers)

    def _is_terminal_expr(self, ply_node):
        return len(ply_node.tail) == 1

    def _handle_terminal_expr(self, ply_node):
        marker = self._build_marker_two(ply_node.tail[0])
        return expr.MarkersExpression([marker])

    def _build_marker_two(self, ply_node):
        name = ply_node.select('name > *')[0]
        if name == 'rule':
            return markers.RuleMarker()
        if name == 'declaration':
            return markers.DeclarationMarker()
        if name == 'selector':
            return markers.SelectorMarker()
        if name == 'block':
            return markers.BlockMarker()
        if self._is_string(name):
            return markers.SymbolMarker(name[1:-1])
        if name == 'property':
            return markers.PropertyMarker()
        if name == 'value':
            return markers.ValueMarker()
        if name == 'eof':
            return markers.EofMarker()
        if name == 'comment':
            return markers.CommentMarker()
        if name == 'csv-comma':
            return markers.CsvCommaMarker()
        if name == 'selector-comma':
            return markers.SelectorCommaMarker()

        repetitions = self._get_repetition(ply_node)
        if name == 'whitespace':
            return markers.WhitespaceMarker(repetitions)
        if name == 'space':
            return markers.SpaceMarker(repetitions)
        if name == 'newline':
            return markers.NewlineMarker(repetitions)
        if name == 'tab':
            return markers.TabMarker(repetitions)

        raise NotImplementedError('Other css marker are not implemented yet')

    def _get_repetition(self, ply_node):
        reps = ply_node.select('repetition > *')
        if len(reps) == 0:
            return 1
        if reps[1] == '*':
            return -1
        return int(reps[1])

    def _is_string(self, str):
        return len(str) > 1 and str[0] == '"' and str[-1] == '"'
