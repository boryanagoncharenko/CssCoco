__author__ = 'boryana'


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