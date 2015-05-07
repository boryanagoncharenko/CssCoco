__author__ = 'boryana'


class Node(object):

    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def has_children(self):
        return True

    def pretty_print(self, level=0, print_indent='  '):
        s = ''.join(['\n', print_indent*level, self.type_, ':'])
        for child in self.value:
            s = ''.join([s, child.pretty_print(level + 1)])
        return s


class TerminalNode(Node):

    def __init__(self, type_, value):
        Node.__init__(self, type_, value)

    def has_children(self):
        return False

    def pretty_print(self, level=0, print_indent='  '):
        return ''.join(['\n', print_indent*level, self.type_, ': \'', self.value, '\''])


class AstBuilder(object):

    @staticmethod
    def build(json):
        builder = AstBuilder()
        node = builder._traverse(json)
        return node

    def _traverse(self, l):
        if type(l) is not list or len(l) == 0:
            raise ValueError('Argument must be a non-empty list')

        if self._is_node_without_children(l):
            return self._get_terminal_node(l)

        children = []
        for i in range(1, len(l)):
            child = self._traverse(l[i])
            children.append(child)
        node_type = l[0]
        return Node(node_type, children)

    def _is_node_without_children(self, l):
        return len(l) == 2 and type(l[1]) is not list

    def _get_terminal_node(self, l):
        node_type = l[0]
        node_value = l[1]
        return TerminalNode(node_type, node_value)


