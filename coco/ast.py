import abc


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

    def get_ignored_markers(self):
        pass

    def get_children(self):
        return self.statements


class WhitespaceContext(Context):

    def __init__(self, statements):
        Context.__init__(self, statements)

    def get_ignored_markers(self):
        pass


class Statement(AstNode):
    """
    Abstract class
    """
    pass


class Declaration(Statement):
    pass


class Rule(Statement):

    def __init__(self, css_markers, ws_options):
        self.css_markers = css_markers
        self.ws_options = ws_options

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        s = ''.join([s, self.css_markers.pretty_print(level + 1)])
        for option in self.ws_options:
            s = ''.join([s, option.pretty_print(level+1)])
        return s


class RequireRule(Rule):

    def __init__(self, css_markers, ws_options):
        Rule.__init__(self, css_markers, ws_options)


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


class Marker(AstNode):
    pass


class CssMarker(Marker):
    pass


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
        markers = children[1:]
        css_markers = self.__get_css_markers(markers)
        ws_options = self.__get_ws_options(markers)

        name = children[0]
        if name.lower() == 'require':
            return RequireRule(css_markers, ws_options)
        raise NotImplementedError('Other rules are not implemented yet')

    def __get_css_markers(self, markers):
        result = []
        for marker in markers:
            success, css_marker = self.__try_get_css_marker(marker)
            if success:
                result.append(css_marker)
        return MarkerSequence(result)

    def __get_ws_options(self, markers):
        option_list = self._get_consecutive_ws_nodes_list(markers)
        result_options = []
        for option in option_list:
            result_options.append(self._build_ws_option_for_consecutive_nodes(option))
        return result_options

    def _get_consecutive_ws_nodes_list(self, markers):
        res = []
        for con_node_list in self._get_consecutive_ws_nodes(markers):
            res.append(con_node_list)
        return res

    def _get_consecutive_ws_nodes(self, markers):
        buffer = []
        for m in markers:
            if self.__is_ws_node(m):
                buffer.append(m)
            else:
                yield buffer
                buffer = []
        yield buffer

    def _build_ws_option_for_consecutive_nodes(self, markers):
        if not markers:
            return MarkerSequenceOption.NONE
        res = []
        for m in markers:
            choices = self._build_choices(m)
            res.append(choices)
        sequences = []
        for s in self._generate_possible_sequences(res, []):
            sequences.append(s)
        return MarkerSequenceOption(sequences)

    def _build_choices(self, ply_node):
        # TODO: this method needs to be revamped
        number_of_children = len(ply_node.tail)
        if number_of_children == 3:
            return [self.__get_ws_marker(ply_node.tail[0]), self.__get_ws_marker(ply_node.tail[2])]
        return [self.__get_ws_marker(ply_node.tail[0])]

    def _generate_possible_sequences(self, option_list, res):
        if len(option_list) == 0:
            yield MarkerSequence(list(res))
        else:
            first_option = option_list[0]
            for option in first_option:
                res.append(option)
                yield from self._generate_possible_sequences(option_list[1:], res)
                del res[-1]

    def __try_get_ws_marker(self, ply_node):
        tail = ply_node.tail
        marker = ply_node.select('ws_marker')
        if len(tail) == 0:
            return False, None

        return True, self.__get_ws_marker(marker)

    def __get_ws_marker_type(self, marker):
        return marker.select('ws_marker > ws_keyword > *')[0].lower()

    def __get_ws_repetitions(self, marker):
        reps = marker.select('ws_marker > repetition > *')
        if len(reps) > 1:
            return int(reps[1])
        return 1

    def __get_ws_marker(self, marker):
        repetition = self.__get_ws_repetitions(marker)
        type = self.__get_ws_marker_type(marker)
        if type == 'space':
            return SpaceMarker(repetition)
        if type == 'newline':
            return NewlineMarker(repetition)
        if type == 'tab_':
            return TabMarker(repetition)
        raise NotImplementedError('Other css marker are not implemented yet')

    def __is_ws_node(self, ply_node):
        marker = ply_node.select('ws_expr')
        return len(marker) != 0

    def __get_option(self, ws_expr):
        pass

    def __try_get_css_marker(self, ply_node):
        marker = ply_node.select('css_marker')
        if len(marker) == 0:
            return False, None

        name = self.__get_css_keyword(marker)
        return True, self.__get_css_marker(name)

    def __get_css_keyword(self, marker):
        return marker[0].select('css_marker > css_keyword > *')[0].lower()

    def __get_css_marker(self, name):
        if name == 'rule':
            return RuleMarker()
        if name == 'declaration':
            return DeclarationMarker()
        if name == 'selector':
            return SelectorMarker()
        if name == 'block':
            return BlockMarker()
        if self.__is_string(name):
            return SymbolMarker(name[1:-1])
        if name == 'value':
            return ValueMarker()
        if name == 'eof_':
            return EofMarker()
        if name == 'comment':
            return CommentMarker()
        raise NotImplementedError('Other css marker are not implemented yet')

    def __is_string(self, str):
        return len(str) > 1 and str[0] == '"' and str[-1] == '"'

