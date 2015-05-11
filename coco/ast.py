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

    def __init__(self, css_markers, ws_markers):
        self.css_markers = css_markers
        self.ws_markers = ws_markers

    def get_children(self):
        return [self.css_markers, self.ws_markers]

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        s = ''.join([s, self.css_markers.pretty_print(level + 1)])
        s = ''.join([s, self.ws_markers.pretty_print(level + 1)])
        return s


class RequireRule(Rule):

    def __init__(self, css_markers, ws_markers):
        Rule.__init__(self, css_markers, ws_markers)


class WhitespaceMarkerSequence(AstNode):
    """
    Todo: this is a weird class
    """
    def __init__(self, before, inner, after):
        self.before = before
        self.inner = inner
        self.after = after

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        s = ''.join([s, '\n', print_indent*(level+1), 'before:', self.before.pretty_print(level + 1)])
        s = ''.join([s, '\n', print_indent*(level+1), 'inner:', self.inner.pretty_print(level + 1)])
        s = ''.join([s, '\n', print_indent*(level+1), 'after:', self.after.pretty_print(level + 1)])
        return s


class Markers(AstNode):

    def __init__(self, markers):
        self.markers = markers

    def __getitem__(self, x):
        return self.markers[x]

    def __iter__(self):
        return self.markers.__iter__()
        # for attr in dir(Foo):
        #     if not attr.startswith("__"):
        #         yield attr

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.markers:
            s = ''.join([s, m.pretty_print(level + 1)])
        return s


class MultiMarkers(AstNode):

    def __init__(self, markers):
        self.markers_list = markers

    def __iter__(self):
        return self.markers_list.__iter__()

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.markers_list:
            s = ''.join([s, m.pretty_print(level + 1)])
        return s


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
        ws_markers = self.__get_ws_markers(markers)
        name = children[0]
        if name.lower() == 'require':
            return RequireRule(css_markers, ws_markers)
        raise NotImplementedError('Other rules are not implemented yet')

    def __get_css_markers(self, markers):
        result = []
        for marker in markers:
            success, css_marker = self.__try_get_css_marker(marker)
            if success:
                result.append(css_marker)
        return Markers(result)

    def __get_ws_markers(self, markers):
        before = self.__get_ws_markers_before(markers)
        inner = self.__get_ws_markers_inner(markers)
        after = self.__get_ws_markers_after(markers)
        return WhitespaceMarkerSequence(before, inner, after)

    def __get_ws_markers_before(self, markers):
        result = []
        for m in markers:
            is_css, _ = self.__try_get_css_marker(m)
            if is_css:
                break
            is_space, space = self.__try_get_ws_marker(m)
            result.append(space)
        return Markers(result)

    def __get_ws_markers_after(self, markers):
        result = []
        for m in markers:
            is_css, _ = self.__try_get_css_marker(m)
            if is_css:
                result = []
            is_space, space = self.__try_get_ws_marker(m)
            if is_space:
                result.append(space)
        return Markers(result)

    def __get_ws_markers_inner(self, markers):
        inner_markers = self.__get_inner_markers(markers)
        result = []
        for ms in self.__get_consecutive_inner_markers(inner_markers):
            result.append(Markers(ms))
        return MultiMarkers(result)

    def __get_consecutive_inner_markers(self, markers):
        buffer = []
        for m in markers:
            is_css, _ = self.__try_get_css_marker(m)
            if is_css:
                yield Markers(buffer)
                buffer = []
            is_space, space = self.__try_get_ws_marker(m)
            if is_space:
                buffer.append(space)
        if len(buffer) > 0:
            yield Markers(buffer)

    def __get_inner_markers(self, markers):
        for i, m in enumerate(markers):
            is_css, _ = self.__try_get_css_marker(m)
            if is_css and i < len(markers) - 1:
                return markers[i+1:]
        return []

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
        raise NotImplementedError('Other css marker are not implemented yet')

    def __is_string(self, str):
        return len(str) > 1 and str[0] == '"' and str[-1] == '"'

    def __try_get_ws_marker(self, ply_node):
        marker = ply_node.select('ws_marker')
        if len(marker) == 0:
            return False, None

        return True, self.__get_ws_marker(marker)

    def __get_ws_marker_type(self, marker):
        return marker[0].select('ws_marker > ws_keyword > *')[0].lower()

    def __get_ws_repetitions(self, marker):
        reps =  marker[0].select('ws_marker > repetition > *')
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
