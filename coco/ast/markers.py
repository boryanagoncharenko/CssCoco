import coco.ast.ast_node as ast


class Marker(ast.AstNode):

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


class PropertyMarker(CssMarker):
    pass


class ValueMarker(CssMarker):
    pass


class EofMarker(CssMarker):
    pass


class CommentMarker(CssMarker):
    pass


class CommaMarker(CssMarker):
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

