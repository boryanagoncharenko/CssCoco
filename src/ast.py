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

    _type_to_value = {'decldelim': ';', 'delim': ','}

    @staticmethod
    def build(json):
        builder = AstBuilder()
        node = builder._traverse(json)
        return node

    def _traverse(self, l):
        if type(l) is not list or len(l) == 0:
            raise ValueError('Argument must be a non-empty list')

        if self._is_node_without_value(l):
            return self._infer_terminal_node(l)

        if self._is_node_without_children(l):
            return self._get_terminal_node(l)

        children = []
        for i in range(1, len(l)):
            child = self._traverse(l[i])
            children.append(child)
        node_type = l[0]
        return Node(node_type, children)

    def _is_node_without_value(self, l):
        return len(l) == 1

    def _infer_terminal_node(self, l):
        node_type = l[0]
        node_value = self._infer_value(node_type)
        return TerminalNode(node_type, node_value)

    def _is_node_without_children(self, l):
        return len(l) == 2 and type(l[1]) is not list

    def _get_terminal_node(self, l):
        node_type = l[0]
        node_value = l[1]
        return TerminalNode(node_type, node_value)

    def _infer_value(self, node_type):
        if node_type not in AstBuilder._type_to_value:
            raise NotImplementedError('Cannot infer value for token type')
        return self._type_to_value[node_type]


class AstTransformer(object):
    # Shall I transform the ast or the json
    # Maybe I need to keep a reference in the child to its parent and its index
    # In this case, transforming the json and building the ast as a last step would be best

    _type_to_value = {'decldelim': ';', 'delim': ','}

    @staticmethod
    def transform(s_expr):
        transformer = AstTransformer(s_expr)
        transformer._traverse(s_expr)
        transformer._traverse_for_whitespace(s_expr, s_expr)
        return s_expr

    def __init__(self, s_expr):
        self._root = s_expr

    def _traverse(self, s_expr):
        if type(s_expr) is not list:
            return

        self._add_value_transformation(s_expr)
        self._block_transformation(s_expr)
        self._declaration_transformation(s_expr)

        i = 1
        while i < len(s_expr):
            self._traverse(s_expr[i])
            i += 1

    def _add_value_transformation(self, s_expr):
        if self._is_expr_without_value(s_expr):
            value = self._get_value(s_expr[0])
            s_expr.append(value)

    def _get_value(self, type_):
        if type_ not in AstTransformer._type_to_value:
            raise NotImplementedError('Cannot infer value for token type')
        return self._type_to_value[type_]

    def _is_expr_without_value(self, s_expr):
        return len(s_expr) == 1

    def _block_transformation(self, s_expr):
        """ Inserts '{' and '}' in a block
        """
        if s_expr[0] == 'block':
            s_expr.insert(1, ['symbol', '{'])
            s_expr.append(['symbol', '}'])

    def _declaration_transformation(self, s_expr):
        """ Inserts ':' between property and value
        """
        if s_expr[0] == 'declaration':
            s_expr.insert(2, ['symbol', ':'])

    # Whitespace nodes should not be the first of the last child of a node, except it if is the root node
    # Moreover spaces should bubble up until the condition above is met
    # The method heavily relies on the assumption that gonzales does not produce two sibling spaces
    def _traverse_for_whitespace(self, current, parent=None, position_in_parent=0):
        if self._has_no_children(current):
            return
        i = 1
        while i < len(current):
            child = current[i]
            abort = self._pull_up_whitespace(child, current, i, parent, position_in_parent)
            if abort:
                return self._traverse_for_whitespace(self._root)
            self._traverse_for_whitespace(child, current, i)
            i += 1

    def _has_no_children(self, s_expr):
        return type(s_expr[1]) is not list

    def _pull_up_whitespace(self, child, current, i, parent, position_in_parent):
        if parent is None or child[0] != 's':
            return False
        if i == 1:
            space = current.pop(i)
            parent.insert(position_in_parent, space)
            return True
        elif i == len(current) - 1:
            space = current.pop(i)
            parent.insert(position_in_parent + 1, space)
            return True
        return False
