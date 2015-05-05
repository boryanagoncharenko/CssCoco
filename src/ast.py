__author__ = 'boryana'


class Node(object):

    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def has_children(self):
        return type(self.value) in [tuple, list]

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.name, ':'])
        for child in self.value:
            s = ''.join([s, child.pretty_print(level + 1)])
        return s

