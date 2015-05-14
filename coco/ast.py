import abc
import src.tree_search as search

class AstNode(object):

    def get_children(self):
        return []

    def get_title(self):
        return self.__class__.__name__

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for child in self.get_children():
            s = ''.join([s, child.pretty_print(level + 1)])
        return s


class Sheet(AstNode):

    def __init__(self, contexts):
        self.contexts = contexts

    def get_children(self):
        return self.contexts


class Context(AstNode):

    def __init__(self, statements):
        self.statements = statements

    def get_children(self):
        return self.statements

    def get_cond_ignores(self):
        pass

    def get_requirement_ignores(self):
        pass

    def get_forbid_ignores(self):
        pass


class WhitespaceContext(Context):

    def __init__(self, statements):
        Context.__init__(self, statements)

    def get_cond_ignores(self):
        return search.CompoundDescriptor.WHITESPACE

    def get_requirement_ignores(self):
        return search.CompoundDescriptor.INDENT

    def get_forbid_ignores(self):
        return search.CompoundDescriptor.INDENT


class Statement(AstNode):
    """
    Abstract class
    """
    pass


class Declaration(Statement):
    pass


class Rule(Statement):

    def __init__(self, markers_list):
        self.markers_list = markers_list

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.markers_list:
            s = ''.join([s, m.pretty_print(level+1)])
        return s


class RequireRule(Rule):

    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class ForbidRule(Rule):

    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class AllowRule(Rule):

    def __init__(self, markers_list):
        Rule.__init__(self, markers_list)


class MarkerSequence(AstNode):

    def __init__(self, markers):
        self.markers = markers

    def __getitem__(self, x):
        return self.markers[x]

    def __iter__(self):
        return iter(self.markers)

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.markers:
            s = ''.join([s, m.pretty_print(level + 1)])
        return s


class MarkerSequenceOption(AstNode):

    def __init__(self, marker_sequences):
        self.marker_sequences = marker_sequences

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for sequence in self.marker_sequences:
            s = ''.join([s, sequence.pretty_print(level + 1)])
        return s

MarkerSequenceOption.NONE = MarkerSequenceOption([])


class Expression(AstNode):

    def get_markers_expression(self):
        pass


class OrExpression(AstNode):

    def __init__(self, markers_list):
        self.markers_list = markers_list

    def get_markers_expression(self):
        return iter(self.markers_list)

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.markers_list:
            s = ''.join([s, m.pretty_print(level+1)])
        return s


class MarkersExpression(AstNode):

    def __init__(self, marker_list):
        self.marker_list = marker_list

    def __iter__(self):
        return iter(self.marker_list)

    def get_markers_expression(self):
        yield self

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.marker_list:
            s = ''.join([s, m.pretty_print(level+1)])
        return s

MarkersExpression.EMPTY = MarkersExpression([])


class Marker(AstNode):

    def is_css_marker(self):
        return False

    def is_ws_marker(self):
        return False


class CssMarker(Marker):

    def is_css_marker(self):
        return True


class DeclarationMarker(CssMarker):
    pass


class SelectorMarker(CssMarker):
    pass


class RuleMarker(CssMarker):

    def __init__(self):
        pass


class BlockMarker(CssMarker):
    pass


class ValueMarker(CssMarker):
    pass


class EofMarker(CssMarker):
    pass


class CommentMarker(CssMarker):
    pass


class SymbolMarker(CssMarker):

    def __init__(self, value):
        self.value = value


class WhitespaceMarker(Marker):

    def __init__(self, repetitions):
        self.repetitions = repetitions

    def is_ws_marker(self):
        return True

    def is_repetitions_set(self):
        return self.repetitions != -1

    @abc.abstractmethod
    def get_value(self):
        pass


class SpaceMarker(WhitespaceMarker):

    def __init__(self, repetitions):
        WhitespaceMarker.__init__(self, repetitions)
        self.__value = ' ' * self.repetitions

    def get_value(self):
        return self.__value


class NewlineMarker(WhitespaceMarker):

    def __init__(self, repetitions):
        WhitespaceMarker.__init__(self, repetitions)
        self.__value = '\n' * self.repetitions

    def get_value(self):
        return self.__value


class TabMarker(WhitespaceMarker):

    def __init__(self, repetitions):
        WhitespaceMarker.__init__(self, repetitions)
        self.__value = '\t' * self.repetitions

    def get_value(self):
        return self.__value


class IndentMarker(WhitespaceMarker):

    def __init__(self, repetitions):
        WhitespaceMarker.__init__(self, repetitions)
        self.__value = '?' * self.repetitions

    def get_value(self):
        return self.__value


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

        name = ply_context.select('context > *')[0]
        if name.lower() == 'whitespace':
            return WhitespaceContext(statements)
        raise NotImplementedError('Other contexts are not implemented yet')

    def __build_rule(self, ply_rule):
        children = ply_rule.select('rule > *')
        markers = self._build_markers(children[1:])
        name = children[0].lower()

        if name == 'require':
            return RequireRule(markers)

        if name == 'forbid':
            return ForbidRule(markers)

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
        if type(left) is OrExpression:
            option_list = option_list + left.markers_list
        else:
            option_list.append(left)

        if type(right) is OrExpression:
            option_list = option_list + right.markers_list
        else:
            option_list.append(right)

        return OrExpression(option_list)


    def _is_parenthesis_expr(self, ply_node):
        return ply_node.tail[0] == '(' and \
            ply_node.tail[-1] == ')'

    def _handle_parenthesis_expr(self, ply_node):
        elements = ply_node.tail[1:-1]
        markers = []
        if len(elements) == 1:
            result = self._build_marker(elements[0])
            if type(result) in [OrExpression, MarkersExpression]:
                return result

        for element in elements:
            markers.append(self._build_marker_two(element))
        return MarkersExpression(markers)

    def _is_terminal_expr(self, ply_node):
        return len(ply_node.tail) == 1

    def _handle_terminal_expr(self, ply_node):
        marker = self._build_marker_two(ply_node.tail[0])
        return MarkersExpression([marker])

    def _build_marker_two(self, ply_node):
        name = ply_node.select('name > *')[0]
        if name == 'rule':
            return RuleMarker()
        if name == 'declaration':
            return DeclarationMarker()
        if name == 'selector':
            return SelectorMarker()
        if name == 'block':
            return BlockMarker()
        if self._is_string(name):
            return SymbolMarker(name[1:-1])
        if name == 'value':
            return ValueMarker()
        if name == 'eof':
            return EofMarker()
        if name == 'comment':
            return CommentMarker()

        repetitions = self._get_repetition(ply_node)
        if name == 'space':
            return SpaceMarker(repetitions)
        if name == 'newline':
            return NewlineMarker(repetitions)
        if name == 'tab':
            return TabMarker(repetitions)

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
