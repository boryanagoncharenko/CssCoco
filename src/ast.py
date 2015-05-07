__author__ = 'boryana'


class Node(object):

    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
        self.parent = None
        self.index = -1

    def has_children(self):
        return True

    def has_parent(self):
        return self.parent is not None

    def pretty_print(self, level=0, print_indent='  '):
        # p = self.parent.type_ if self.has_parent() else 'none' | , p, ' i=', str(self.index)
        s = ''.join(['\n', print_indent*level, self.type_, ':'])
        for child in self.value:
            s = ''.join([s, child.pretty_print(level + 1)])
        return s

    def __repr__(self):
        parent_type = self.parent.type_ if self.has_parent() else 'none'
        return ''.join([' Node(type=', self.type_, ', parent=', parent_type, ' index=', str(self.index), ')'])


class TerminalNode(Node):

    def __init__(self, type_, value):
        Node.__init__(self, type_, value)

    def has_children(self):
        return False

    def pretty_print(self, level=0, print_indent='  '):
        # p = self.parent.type_ if self.parent is not None else 'none' | , ' p=', p, ' i=', str(self.index)
        return ''.join(['\n', print_indent*level, self.type_, ': \'', self.value, '\''])


class AstBuilder(object):

    @staticmethod
    def build(json):
        builder = AstBuilder()
        node = builder._traverse(json)
        builder._annotate_ast(node)
        return node

    def _traverse(self, l):
        if type(l) is not list or len(l) == 0:
            raise ValueError('Argument must be a non-empty list')

        if AstBuilder._is_terminal(l):
            node_type = l[0]
            node_value = l[1]
            return TerminalNode(node_type, node_value)

        children = []
        for i in range(1, len(l)):
            child = self._traverse(l[i])
            children.append(child)
        node_type = l[0]
        return Node(node_type, children)

    @staticmethod
    def _is_terminal(l):
        return len(l) == 2 and type(l[1]) is not list

    def _annotate_ast(self, node):
        if not node.has_children():
            return
        for index, child in enumerate(node.value):
            child.parent = node
            child.index = index
            self._annotate_ast(child)
