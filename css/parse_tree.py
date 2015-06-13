import abc
import coco.analysis.values as values


class NodeAbstract(object):
    pass


class NodeFilter(NodeAbstract):
    def __init__(self, node, filter_seqs):
        self._node = node
        self._filter_seqs = filter_seqs
        self.type_ = self._node.type



class Node(NodeAbstract):

    _print_indent = '  '

    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
        self.parent = None
        self.index = -1
        self.start_position = None
        self.end_position = None
        self._api = {}
        self._register_api()

    def _register_api(self):
        pass

    def has_method(self, property_name):
        return property_name in self._api

    def invoke_method_with_arg(self, property_name, argument):
        return self._api[property_name](argument)

    def invoke_method(self, property_name):
        return self._api[property_name]()

    def has_children(self):
        return True

    def has_parent(self):
        return self.parent is not None

    def pretty_print(self, level=0, verbose=False):
        s = ''.join(['\n', Node._print_indent*level, self.type_, ':'])
        if verbose:
            s = ''.join([s, self.get_position_str()])
        for child in self.value:
            s = ''.join([s, child.pretty_print(level + 1, verbose)])
        return s

    def get_position_str(self):
        return ''.join([' start[', str(self.start_position.line), ':', str(self.start_position.column), ']',
                        'end[',  str(self.end_position.line), ':', str(self.end_position.column), ']'])

    def __repr__(self):
        parent_type = self.parent.type_ if self.has_parent() else 'none'
        return ''.join([' Node(type=', self.type_, ', parent=', parent_type, ' index=', str(self.index), ')'])

    def to_error_string(self):
        string = ''
        for child in self.value:
            string = ''.join([string, child.to_error_string()])
        return string

    def _get_terminal_nodes(self):
        for child in self.value:
            yield from child._get_terminal_nodes()


class TerminalNode(Node):

    def __init__(self, type_, value):
        super(TerminalNode, self).__init__(type_, value)

    def _register_api(self):
        self._api['value'] = self._get_value

    def has_children(self):
        return False

    def pretty_print(self, level=0, verbose=False):
        s = ''.join(['\n', Node._print_indent*level, self.type_, ': \'', self.value, '\''])
        if verbose:
            s = ''.join([s, self.get_position_str()])
        return s

    def to_error_string(self):
        return self.value

    def _get_terminal_nodes(self):
        yield self

    def _get_value(self):
        return values.String(self.value)


class Declaration(Node):

    def __init__(self, value):
        super(Declaration, self).__init__('declaration', value)

    def _register_api(self):
        self._api['is-vendor-specific'] = self.is_vendor_specific
        self._api['say'] = self.say

    def is_vendor_specific(self):
        return values.Boolean.TRUE

    def say(self, param):
        return values.String(param.value)


class Property(Node):

    def __init__(self, value):
        super(Property, self).__init__('property', value)

    def _register_api(self):
        self._api['name'] = self._name

    def _name(self):
        return values.String(self.value[0].value)


class CombinatorSelector(Node):
    pass


class ChildSelector(CombinatorSelector):
    pass


class DescendantSelector(CombinatorSelector):
    pass


class AdjacentSiblingSelector(CombinatorSelector):
    pass


class GeneralSiblingSelector(CombinatorSelector):
    pass


class SimpleSelector(Node):
    pass


class ElementSelector(SimpleSelector):
    def __init__(self, name):
        super(ElementSelector, self).__init__()
        self.name = name

    def _register_api(self):
        return {'name': self.name}


class IdSelector(SimpleSelector):
    pass


class ClassSelector(SimpleSelector):
    pass


class AttributeSelector(SimpleSelector):
    pass


class UniversalSelector(SimpleSelector):
    pass


class PseudoSelector(SimpleSelector):
    pass


class String(TerminalNode):

    def __init__(self, type_, value):
        super(String, self).__init__(type_, value)

    def has_single_quotes(self):
        return self.value[0] == '\''

    def has_double_quotes(self):
        return not self.has_single_quotes()


class Position(object):

    def __init__(self, line, column):
        self.line = line
        self.column = column

    def get_next_position(self, value):
        num_newlines = value.count('\n')
        if num_newlines > 0:
            return Position(self.line+num_newlines, 1)
        return Position(self.line, self.column+len(value))

Position.START = Position(1, 1)


class ParseTreeBuilder(object):

    @staticmethod
    def build(json):
        builder = ParseTreeBuilder()
        node = builder._build(json)
        builder._annotate_ast(node)
        return node

    def _build(self, l):
        if type(l) is not list or len(l) == 0:
            raise ValueError('Argument must be a non-empty list')

        if self._is_terminal(l):
            node_type = l[0]
            node_value = l[1]
            return TerminalNode(node_type, node_value)

        children = []
        for i in range(1, len(l)):
            child = self._build(l[i])
            child.index = i - 1
            children.append(child)
        node_type = l[0]
        if node_type == 'declaration':
            return Declaration(children)
        if node_type == 'property':
            return Property(children)
        return Node(node_type, children)

    def _is_terminal(self, l):
        return len(l) == 2 and type(l[1]) is not list

    def _annotate_ast(self, node):
        self._add_parent_and_child_index(node)
        self._add_position_to_terminal_nodes(node)
        self._add_position_to_nodes(node)

    def _add_parent_and_child_index(self, node):
        if not node.has_children():
            return
        for index, child in enumerate(node.value):
            child.parent = node
            # child.index = index
            self._annotate_ast(child)

    def _add_position_to_terminal_nodes(self, node):
        start = Position.START
        for terminal in node._get_terminal_nodes():
            terminal.start_position = start
            terminal.end_position = start.get_next_position(terminal.value)
            start = Position(terminal.end_position.line, terminal.end_position.column)

    def _add_position_to_nodes(self, node):
        if node.has_children():
            for child in node.value:
                self._add_position_to_nodes(child)

            first_child = node.value[0]
            last_child = node.value[-1]
            node.start_position = first_child.start_position
            node.end_position = last_child.end_position
