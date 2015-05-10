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

    def __init__(self, css_markers, space_markers):
        self.css_markers = css_markers
        self.space_markers = space_markers

    def get_children(self):
        return [self.css_markers, self.space_markers]

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for css_marker in self.css_markers:
            s = ''.join([s, css_marker.pretty_print(level + 1)])
        s = ''.join([s, self.space_markers.pretty_print(level + 1)])
        return s


class RequireRule(Rule):

    def __init__(self, css_markers, space_markers):
        Rule.__init__(self, css_markers, space_markers)


class SpaceMarkerSequence(AstNode):
    """
    Todo: this class contains too much and the pretty_print methods illustrates this
    """
    def __init__(self, before, inner, after):
        self.before = before
        self.inner = inner
        self.after = after

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        s = ''.join([s, '\n', print_indent*(level + 1), 'before:'])
        for b in self.before:
            s = ''.join([s, b.pretty_print(level + 2)])
        s = ''.join([s, '\n', print_indent*(level + 1), 'inner:'])
        for i in self.inner:
            s = ''.join([s, '['])
            for element in i:
                s = ''.join([s, element.pretty_print(level + 2)])
            s = ''.join([s, ']'])
        s = ''.join([s, '\n', print_indent*(level + 1), 'after:'])
        for a in self.after:
            s = ''.join([s, a.pretty_print(level + 2)])
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


class WhitespaceMarker(Marker):
    pass


class SpaceMarker(WhitespaceMarker):
    pass


class NewlineMarker(WhitespaceMarker):
    pass


class TabMarker(WhitespaceMarker):
    pass


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
        space_markers = self.__get_space_markers(markers)
        name = children[0]
        if name.lower() == 'require':
            return RequireRule(css_markers, space_markers)
        raise NotImplementedError('Other rules are not implemented yet')

    def __get_css_markers(self, markers):
        result = []
        for marker in markers:
            success, css_marker = self.__try_get_css_marker(marker)
            if success:
                result.append(css_marker)
        return result

    def __get_space_markers(self, markers):
        before = self.__get_space_markers_before(markers)
        inner = self.__get_space_markers_inner(markers)
        after = self.__get_space_markers_after(markers)
        return SpaceMarkerSequence(before, inner, after)

    def __get_space_markers_before(self, markers):
        result = []
        for m in markers:
            is_css, _ = self.__try_get_css_marker(m)
            if is_css:
                break
            is_space, space = self.__try_get_space_marker(m)
            result.append(space)
        return result

    def __get_space_markers_after(self, markers):
        result = []
        for m in markers:
            is_css, _ = self.__try_get_css_marker(m)
            if is_css:
                result = []
            is_space, space = self.__try_get_space_marker(m)
            if is_space:
                result.append(space)
        return result

    def __get_space_markers_inner(self, markers):
        inner_markers = self.__get_inner_markers(markers)
        result = []
        buffer = []
        for m in inner_markers:
            is_css, _ = self.__try_get_css_marker(m)
            if is_css:
                result.append(buffer)
                buffer = []
            is_space, space = self.__try_get_space_marker(m)
            if is_space:
                buffer.append(space)
        return result

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

        name = marker[0].select('css_marker > *')[0].lower()
        return True, self.__get_css_marker(name)

    def __get_css_marker(self, name):
        if name == 'rule':
            return RuleMarker()
        if name == 'declaration':
            return DeclarationMarker()
        if name == 'selector':
            return SelectorMarker()
        raise NotImplementedError('Other css marker are not implemented yet')

    def __try_get_space_marker(self, ply_node):
        marker = ply_node.select('space_marker')
        if len(marker) == 0:
            return False, None

        name = marker[0].select('space_marker > *')[0].lower()
        return True, self.__get_space_marker(name)

    def __get_space_marker(self, name):
        if name == 'space':
            return SpaceMarker()
        if name == 'newline':
            return NewlineMarker()
        if name == 'tab_':
            return TabMarker()
        raise NotImplementedError('Other css marker are not implemented yet')
