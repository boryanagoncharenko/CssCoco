from csscoco import coco as ast


class Expression(ast.AstNode):

    def get_markers_expression(self):
        pass


class OrExpression(ast.AstNode):

    def __init__(self, markers_list):
        self.markers_list = markers_list

    def get_markers_expression(self):
        return iter(self.markers_list)

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.get_title(), ':'])
        for m in self.markers_list:
            s = ''.join([s, m.pretty_print(level+1)])
        return s


class MarkersExpression(ast.AstNode):

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