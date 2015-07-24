from csscoco.lang.analysis import values as values


class CssNode(object):
    def __init__(self, type_, value, categories=None):
        self.parent = None
        self.type_ = type_
        self.value = value
        self.search_labels = self.initialize_labels(type_, categories)
        self.index = -1
        self.start_position = None
        self.end_position = None
        self._api = {}
        self._register_api()
        self._print_indent = '  '

    def initialize_labels(self, type_, categories):
        if not categories:
            return [type_]
        return [type_] + categories

    def matches(self, value):
        return value in self.search_labels

    def has_method(self, property_name):
        return property_name in self._api

    def invoke_method(self, method_name, argument):
        return self._api[method_name](argument)

    def invoke_property(self, property_name):
        return self._api[property_name]()

    def has_children(self):
        return True

    def pretty_print(self, level=0, verbose=False):
        s = ''.join(['\n', self._print_indent*level, self.type_, ':'])
        if verbose:
            s = ''.join([s, self.get_position_str()])
        for child in self.value:
            s = ''.join([s, child.pretty_print(level + 1, verbose)])
        return s

    def get_position_str(self):
        return ''.join([' start[', str(self.start_position.line), ':', str(self.start_position.column), ']',
                        'end[',  str(self.end_position.line), ':', str(self.end_position.column), ']'])

    def _get_terminal_nodes(self):
        for child in self.value:
            yield from child._get_terminal_nodes()

    def _register_api(self):
        self._api['string'] = self._get_string
        self._api['child'] = self._get_child

    def _get_string(self):
        res = ''
        for v in self.value:
            res = ''.join([res, v._get_string().value])
        return values.String(res)

    def _get_child(self, i):
        return values.Node(self.value[i])

    def _get_value(self):
        return self.value


class TerminalCssNode(CssNode):
    def __init__(self, type_, value, categories=None):
        super(TerminalCssNode, self).__init__(type_, value, categories)

    def has_children(self):
        return False

    def pretty_print(self, level=0, verbose=False):
        s = ''.join(['\n', self._print_indent*level, self.type_, ': \'', self.value, '\''])
        if verbose:
            s = ''.join([s, self.get_position_str()])
        return s

    def to_error_string(self):
        return self.value

    def _register_api(self):
        super(TerminalCssNode, self)._register_api()
        self._api['value'] = self._get_value

    def _get_string(self):
        return values.String(self.value)

    def _get_terminal_nodes(self):
        yield self

    def _get_value(self):
        return values.String(self.value)


class Declaration(CssNode):
    def __init__(self, value):
        super(Declaration, self).__init__('declaration', value)

    def _register_api(self):
        super(Declaration, self)._register_api()
        self._api['property'] = self._get_property
        self._api['value'] = self._get_value
        self._api['is-vendor-specific'] = self._is_vendor_specific

    def _get_property(self):
        return values.Node(self.value[0])

    def _get_value(self):
        for i in range(1, len(self.value), 1):
            if type(self.value[-i]) is not TerminalCssNode:
                return values.Node(self.value[-i])

    def _is_vendor_specific(self):
        return self.value[0]._is_vendor_specific()


class Property(TerminalCssNode):
    def __init__(self, name):
        super(Property, self).__init__('property', name)
        self._name = name
        self._is_vendor = None
        self._vendor_prefixes = {'-ms-', 'mso-', '-moz-', '-o-', '-atsc-', '-wap-', '-webkit-', '-khtml-'}

    def _register_api(self):
        super(Property, self)._register_api()
        self._api['name'] = self._get_name
        self._api['is-vendor-specific'] = self._is_vendor_specific
        self._api['standard'] = self._get_standard

    def _get_string(self):
        return values.String(self._name)

    def _get_name(self):
        return values.String(self._name)

    def _is_vendor_specific(self):
        if not self._is_vendor:
            prefix = self._check_is_vendor()
            self._is_vendor = values.Boolean.build(prefix)
        return self._is_vendor

    def _get_standard(self):
        if self._is_vendor_specific().value:
            prefix = self._check_is_vendor()
            return values.String(self._name[len(prefix):])
        return self._get_name()

    def _check_is_vendor(self):
        for p in self._vendor_prefixes:
            prefix_slice = self._name[:len(p)].lower()
            if prefix_slice.startswith(p):
                return p
        return None


class CombinatorSelector(CssNode):
    pass


class ChildSelector(CombinatorSelector):
    pass


class DescendantSelector(CombinatorSelector):
    pass


class AdjacentSiblingSelector(CombinatorSelector):
    pass


class GeneralSiblingSelector(CombinatorSelector):
    pass


class SimpleSelector(TerminalCssNode):
    def __init__(self, type_, name):
        super(SimpleSelector, self).__init__(type_, name, categories=['selectorpart'])
        self._api['name'] = self._get_value


class ElementSelector(SimpleSelector):
    def __init__(self, name):
        super(ElementSelector, self).__init__('tag', name)


class IdSelector(SimpleSelector):
    def __init__(self, name):
        super(IdSelector, self).__init__('id', name)


class ClassSelector(SimpleSelector):
    def __init__(self, name):
        super(ClassSelector, self).__init__('class', name)


class AttributeSelector(CssNode):
    def __init__(self, children):
        super(AttributeSelector, self).__init__('attribute-selector', children)
        self.attribute = children[0]
        self.selector = children[1] if len(children) > 1 else None
        self.attr_value = children[2] if len(children) > 2 else None

    def _register_api(self):
        super(AttributeSelector, self)._register_api()
        self._api['value'] = self._get_value

    def _get_value(self):
        if self.attr_value:
            return values.Node(self.attr_value)
        return values.Undefined.VALUE


class Attribute(TerminalCssNode):
    def __init__(self, value):
        super(Attribute, self).__init__('attribute', value)


class Function(CssNode):
    def __init__(self, value):
        super(Function, self).__init__(value[0].value, value, categories=['function'])

    def _register_api(self):
        super(Function, self)._register_api()
        self._api['name'] = self._get_name

    def _get_name(self):
        return values.String(self.value[0].value)


class Rgba(Function):
    def __init__(self, value):
        super(Rgba, self).__init__(value)

    def _register_api(self):
        super(Rgba, self)._register_api()
        self._api['opacity'] = self._get_opacity

    def _get_opacity(self):
        return values.Integer(float(self.value[1].value[-1].value))


class Hex(TerminalCssNode):
    def __init__(self, value):
        super(Hex, self).__init__('hex', value)
        self._is_long = len(self.value) > 4

    def _register_api(self):
        super(Hex, self)._register_api()
        self._api['is-long'] = self._get_is_long

    def _get_is_long(self):
        return values.Boolean.build(self._is_long)


class Number(TerminalCssNode):
    def __init__(self, value, float_value):
        super(Number, self).__init__('number', value)
        self.float_value = float_value

    def _register_api(self):
        super(Number, self)._register_api()
        self._api['num-value'] = self._get_value

    def _get_value(self):
        return values.Integer(self.float_value)


class String(TerminalCssNode):
    def __init__(self, value):
        super(String, self).__init__('string', value)

    def _register_api(self):
        super(String, self)._register_api()
        self._api['has-single-quotes'] = self._has_single_quotes
        self._api['has-double-quotes'] = self._has_double_quotes

    def _get_string(self):
        return values.String(self.value)

    def _has_single_quotes(self):
        return values.Boolean.build(self.value[0] == "'")

    def _has_double_quotes(self):
        return values.Boolean.build(self.value[0] == '"')


class Dimension(CssNode):
    def __init__(self, value):
        super(Dimension, self).__init__('dimension', value)

    def _register_api(self):
        super(Dimension, self)._register_api()
        self._api['unit'] = self._get_unit

    def _get_unit(self):
        return values.String(self.value[1].value)


class AtRule(CssNode):
    pass


class RuleSet(CssNode):
    def __init__(self, value):
        super(RuleSet, self).__init__('ruleset', value)
        self._api['is-single-line'] = self._is_single_line

    def _is_single_line(self):
        is_single_line = self.value[0].start_position.line == self.value[-1].end_position.line
        return values.Boolean.build(is_single_line)


class Charset(AtRule):
    def __init__(self, value):
        super(Charset, self).__init__('charset', value)


class Import(AtRule):
    def __init__(self, value):
        super(Import, self).__init__('import', value)


class FontFace(AtRule):
    def __init__(self, value):
        super(FontFace, self).__init__('fontface', value)


class ParseTreeBuilder(object):

    @staticmethod
    def build(json):
        builder = ParseTreeBuilder()
        node = builder._build(json)
        builder._annotate_ast(node)
        return node

    def _build(self, l):
        if self._is_symbol(l):
            return TerminalCssNode('symbol', l)
        if len(l) == 0:
            raise ValueError('S-expr argument must be a non-empty list.')

        if self._is_terminal(l):
            return self._get_terminal(l)

        return self._get_non_terminal(l)

    def _is_terminal(self, l):
        return len(l) == 2 and type(l[1]) is not list

    def _is_symbol(self, l):
        return type(l) is not list

    def _get_children(self, l):
        children = []
        for i in range(1, len(l)):
            child = self._build(l[i])
            child.index = i - 1
            children.append(child)
        return children

    def _get_terminal(self, l):
        node_type = l[0]
        node_value = l[1]
        if node_type == 'shash':
            return IdSelector(node_value)
        if node_type == 'tag':
            return ElementSelector(node_value)
        if node_type == 'vhash':
            return Hex(node_value)
        if node_type == 'number':
            number_value = float(node_value)
            return Number(node_value, number_value)
        if node_type == 'string':
            return String(node_value)
        if node_type == 'delim':
            pass
        return TerminalCssNode(node_type, node_value)

    def _get_non_terminal(self, l):
        children = self._get_children(l)
        node_type = l[0]
        if node_type == 'declaration':
            return Declaration(children)
        if node_type == 'property':
            assert len(children) == 1
            return Property(children[-1].value)
        if node_type == 'clazz':
            assert len(children) == 1
            return ClassSelector(children[-1].value)
        if node_type == 'attrib':
            return self._get_attribute(children)
        if node_type == 'funktion' and l[1][1] == 'rgba':
            return Rgba(children)
        if node_type == 'funktion':
            return Function(children)
        if node_type == 'funktion':
            return Function(children)
        if node_type == 'atrules' or node_type == 'atruler':
            return self._get_at_rule(children)
        if node_type == 'ruleset':
            return RuleSet(children)
        if node_type == 'dimension':
            return Dimension(children)
        return CssNode(node_type, children)

    def _get_attribute(self,children):
        assert len(children) == 3 or len(children) == 1
        children[0] = Attribute(children[0].value)
        if len(children) == 3:
            children[2].search_labels.append('attribute-value')
        return AttributeSelector(children)

    def _get_at_rule(self, children):
        keyword = children[0].value[0].value
        if keyword == 'charset':
            children.pop(0)
            return Charset(children)
        if keyword == 'import':
            children.pop(0)
            return Import(children)
        if keyword == 'font-face':
            children.pop(0)
            return FontFace(children)
        raise NotImplementedError()

    def _annotate_ast(self, node):
        # TODO: what on earth have I done here? terminals' positions should be done while building
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


class CssPattern(object):
    def __init__(self, keys=None):
        self._id_to_node = {}
        if keys:
            self._id_to_node = keys

    def register_node(self, identifier, node):
        self._id_to_node[identifier] = node

    def unregister_node(self, identifier):
        self._id_to_node.pop(identifier)

    def register_multi_nodes(self, relations, nodes):
        for i, r in enumerate(relations):
            self._id_to_node[r.target_node] = nodes[i]

    def unregister_multi_nodes(self, relations):
        for r in relations:
            self._id_to_node.pop(r.target_node)

    def __getitem__(self, item):
        return self._id_to_node[item]

    def __iter__(self):
        return iter(self._id_to_node)

    def copy(self):
        return CssPattern(self._id_to_node.copy())
