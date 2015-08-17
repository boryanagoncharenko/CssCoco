import csscoco.lang.analysis.values as values
from csscoco.lang.common_ import ExprConstants


class CssNode(object):
    print_indent = '  '

    def __init__(self, value, categories=None):
        self.parent = None
        self.value = value
        self._categories = ['any']
        self.start_position = None
        self.end_position = None
        self._api = {}
        self._register_api()
        self.index = -1
        if categories:
            self._categories.extend(categories)

    def extend_categories(self, category):
        self._categories.insert(-1, category)

    def get_type(self):
        return self._categories[-1]

    def matches(self, value):
        return value in self._categories

    def has_method(self, property_name):
        return property_name in self._api

    def invoke_method(self, method_name, argument):
        return self._api[method_name](argument)

    def invoke_property(self, property_name):
        return self._api[property_name]()

    def has_children(self):
        return True

    def pretty_print(self, level=0, verbose=False):
        s = ''.join(['\n', self.print_indent*level, self._categories[-1], ':'])
        if verbose:
            s = ''.join([s, self.get_position_str()])
        for child in self.value:
            s = ''.join([s, child.pretty_print(level + 1, verbose)])
        return s

    def get_position_str(self):
        return ''.join([' start[', str(self.start_position.line), ':', str(self.start_position.column), ']',
                        'end[',  str(self.end_position.line), ':', str(self.end_position.column), ']'])

    def _register_api(self):
        self._api[ExprConstants.STRING] = self._get_string
        self._api[ExprConstants.CHILD] = self._get_child

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
    def __init__(self, value, categories=None):
        super(TerminalCssNode, self).__init__(value)
        if categories:
            self._categories.extend(categories)

    def has_children(self):
        return False

    def pretty_print(self, level=0, verbose=False):
        s = ''.join(['\n', self.print_indent*level, self._categories[-1], ': \'', self.value, '\''])
        if verbose:
            s = ''.join([s, self.get_position_str()])
        return s

    def to_error_string(self):
        return self.value

    def _register_api(self):
        super(TerminalCssNode, self)._register_api()
        self._api[ExprConstants.VALUE] = self._get_value

    def _get_string(self):
        return values.String(self.value)

    def _get_terminal_nodes(self):
        yield self

    def _get_value(self):
        return values.String(self.value)


class Stylesheet(CssNode):
    def __init__(self, children):
        super(Stylesheet, self).__init__(children)
        self._categories.append('stylesheet')


class Declaration(CssNode):
    def __init__(self, children):
        super(Declaration, self).__init__(children)
        self._categories.append('declaration')

    def _register_api(self):
        super(Declaration, self)._register_api()
        self._api[ExprConstants.PROPERTY] = self._get_property
        self._api[ExprConstants.VALUE] = self._get_value
        self._api[ExprConstants.IS_VENDOR_SPECIFIC] = self._is_vendor_specific

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
        super(Property, self).__init__(name)
        self._categories.append('property')
        self._name = name
        self._is_vendor = None
        self._vendor_prefixes = {'-ms-', 'mso-', '-moz-', '-o-', '-atsc-', '-wap-', '-webkit-', '-khtml-'}

    def _register_api(self):
        super(Property, self)._register_api()
        self._api[ExprConstants.NAME] = self._get_name
        self._api[ExprConstants.IS_VENDOR_SPECIFIC] = self._is_vendor_specific
        self._api[ExprConstants.STANDARD] = self._get_standard

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


class SimpleSelector(CssNode):
    def __init__(self, value):
        super(SimpleSelector, self).__init__(value)
        self._categories.append('simple-selector')


class CombinatorSelector(CssNode):
    def __init__(self, name):
        super(CombinatorSelector, self).__init__(name)
        self._categories.append('combinator')


class ChildSelector(CombinatorSelector):
    def __init__(self, name):
        super(ChildSelector, self).__init__(name)
        self._categories.append('child-selector')


class DescendantSelector(CombinatorSelector):
    def __init__(self, name):
        super(DescendantSelector, self).__init__(name)
        self._categories.append('descendant-selector')


class SelectorPart(TerminalCssNode):
    def __init__(self, name):
        super(SelectorPart, self).__init__(name)
        self._categories.append('selector-part')

    def _register_api(self):
        super(SelectorPart, self)._register_api()
        self._api[ExprConstants.IS_KEY] = self._get_is_key
        self._api[ExprConstants.NAME] = self._get_value

    def _get_is_key(self):
        r = self.index == len(self.parent.value) - 1
        return values.Boolean.build(r)


class ElementSelectorPart(SelectorPart):
    def __init__(self, name):
        super(ElementSelectorPart, self).__init__(name)
        self._categories.append('tag')


class HeadingSelector(ElementSelectorPart):
    def __init__(self, name):
        super(HeadingSelector, self).__init__(name)
        self._categories.append('heading')


class IdSelectorPart(SelectorPart):
    def __init__(self, name):
        super(IdSelectorPart, self).__init__(name)
        self._categories.append('id')


class ClassSelectorPart(SelectorPart):
    def __init__(self, name):
        super(ClassSelectorPart, self).__init__(name)
        self._categories.append('class')


class AttributeSelector(CssNode):
    def __init__(self, children):
        super(AttributeSelector, self).__init__(children)
        self._categories.append('attribute-selector')
        self.attribute = children[0]
        self.selector = children[1] if len(children) > 1 else None
        self.attr_value = children[2] if len(children) > 2 else None

    def _register_api(self):
        super(AttributeSelector, self)._register_api()
        self._api[ExprConstants.VALUE] = self._get_value
        self._api[ExprConstants.IS_KEY] = self._get_is_key

    def _get_value(self):
        return values.Node(self.attr_value)

    def _get_is_key(self):
        r = self.index == len(self.parent.value) - 1
        return values.Boolean.build(r)


class Attribute(TerminalCssNode):
    def __init__(self, value):
        super(Attribute, self).__init__(value)
        self._categories.append('attribute')


class AttributeSelectorType(TerminalCssNode):
    def __init__(self, value):
        super(AttributeSelectorType, self).__init__(value)
        self._categories.append('attribute-selector-type')


class Function(CssNode):
    def __init__(self, children):
        super(Function, self).__init__(children)
        self._categories.append('function')

    def _register_api(self):
        super(Function, self)._register_api()
        self._api[ExprConstants.NAME] = self._get_name

    def _get_name(self):
        return values.String(self.value[0].value)


class Rgba(Function):
    def __init__(self, value):
        super(Rgba, self).__init__(value)
        self._categories.extend(['color', 'rgba'])

    def _register_api(self):
        super(Rgba, self)._register_api()
        self._api[ExprConstants.OPACITY] = self._get_opacity

    def _get_opacity(self):
        return values.Integer(float(self.value[1].value[-1].value))


class Rgb(Function):
    def __init__(self, value):
        super(Rgb, self).__init__(value)
        self._categories.extend(['color', 'rgb'])


class Hsla(Function):
    def __init__(self, value):
        super(Hsla, self).__init__(value)
        self._categories.extend(['color', 'hsla'])


class Hsl(Function):
    def __init__(self, value):
        super(Hsl, self).__init__(value)
        self._categories.extend(['color', 'hsl'])


class Hex(TerminalCssNode):
    def __init__(self, value):
        super(Hex, self).__init__(value)
        self._categories.extend(['color', 'hex'])
        self._is_long = len(self.value) > 4

    def _register_api(self):
        super(Hex, self)._register_api()
        self._api[ExprConstants.IS_LONG] = self._get_is_long

    def _get_is_long(self):
        return values.Boolean.build(self._is_long)


class ColorName(TerminalCssNode):
    def __init__(self, value):
        super(ColorName, self).__init__(value)
        self._categories.extend(['color', 'colorname'])
        self._is_long = len(self.value) > 4


class Number(TerminalCssNode):
    def __init__(self, value, float_value):
        super(Number, self).__init__(value)
        self._categories.append('number')
        self.float_value = float_value

    def _register_api(self):
        super(Number, self)._register_api()
        self._api[ExprConstants.NUM_VALUE] = self._get_value

    def _get_value(self):
        return values.Integer(self.float_value)


class String(TerminalCssNode):
    def __init__(self, value):
        super(String, self).__init__(value)
        self._categories.append('string')

    def _register_api(self):
        super(String, self)._register_api()
        self._api[ExprConstants.HAS_SINGLE_QUOTES] = self._has_single_quotes
        self._api[ExprConstants.HAS_DOUBLE_QUOTES] = self._has_double_quotes

    def _get_string(self):
        return values.String(self.value)

    def _has_single_quotes(self):
        return values.Boolean.build(self.value[0] == "'")

    def _has_double_quotes(self):
        return values.Boolean.build(self.value[0] == '"')


class Dimension(CssNode):
    def __init__(self, value):
        super(Dimension, self).__init__(value)
        self._categories.append('dimension')

    def _register_api(self):
        super(Dimension, self)._register_api()
        self._api[ExprConstants.UNIT] = self._get_unit

    def _get_unit(self):
        return values.String(self.value[1].value)


class AtRule(CssNode):
    def __init__(self, children):
        super(AtRule, self).__init__(children)
        self._categories.append('atrule')


class RuleSet(CssNode):
    def __init__(self, children):
        super(RuleSet, self).__init__(children)
        self._categories.append('ruleset')
        self._api[ExprConstants.IS_SINGLE_LINE] = self._is_single_line

    def _is_single_line(self):
        is_single_line = self.value[0].start_position.line == self.value[-1].end_position.line
        return values.Boolean.build(is_single_line)


class Charset(AtRule):
    def __init__(self, value):
        super(Charset, self).__init__(value)
        self._categories.append('charset')


class Import(AtRule):
    def __init__(self, value):
        super(Import, self).__init__(value)
        self._categories.append('import')


class FontFace(AtRule):
    def __init__(self, value):
        super(FontFace, self).__init__(value)
        self._categories.append('fontface')


class Media(AtRule):
    def __init__(self, value):
        super(Media, self).__init__(value)
        self._categories.append('media')


class Uri(CssNode):
    def __init__(self, value):
        super(Uri, self).__init__(value)
        self._categories.append('uri')

    def _register_api(self):
        super(Uri, self)._register_api()
        self._api[ExprConstants.ARGUMENT] = self._get_argument

    def _get_argument(self):
        return values.Node(self.value[1])


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
            return IdSelectorPart(node_value)
        if node_type == 'tag':
            return self._get_element_selector(node_type, node_value)
        if node_type == 'vhash':
            return Hex(node_value)
        if node_type == 'number':
            number_value = float(node_value)
            return Number(node_value, number_value)
        if node_type == 'string':
            return String(node_value)
        if node_type == 'ident' and CssLookUp.is_color_name(node_value):
            return ColorName(node_value)
        if node_type == 'attrselector':
            return AttributeSelectorType(node_value)
        return TerminalCssNode(node_value, categories=[node_type])

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
            return ClassSelectorPart(children[-1].value)
        if node_type == 'attrib':
            return self._get_attribute(children)
        if node_type == 'funktion':
            return self._get_function(l, children)
        if node_type in ['atrules', 'atruler', 'atruleb']:
            return self._get_at_rule(children)
        if node_type == 'ruleset':
            return RuleSet(children)
        if node_type == 'dimension':
            return Dimension(children)
        if node_type == 'simpleselector':
            return SimpleSelector(children)
        if node_type == 'uri':
            return Uri(children)
        return CssNode(children, categories=[node_type])

    def _get_element_selector(self, node_type, node_value):
        if CssLookUp.is_heading(node_value):
            return HeadingSelector(node_value)
        return ElementSelectorPart(node_value)

    def _get_function(self, l, children):
        function_name = l[1][1].lower()
        if function_name == 'rgba':
            return Rgba(children)
        if function_name == 'hsla':
            return Hsla(children)
        if function_name == 'rgb':
            return Rgb(children)
        if function_name == 'hsl':
            return Hsl(children)
        return Function(children)

    def _get_attribute(self, children):
        assert len(children) == 3 or len(children) == 1
        children[0] = Attribute(children[0].value)
        if len(children) == 3:
            children[2].extend_categories('attribute-value')
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
        if keyword == 'media':
            children.pop(0)
            return Media(children)
        raise NotImplementedError()

    def _annotate_ast(self, node):
        start = Position.START
        frontier = [node]
        while frontier:
            current = frontier[-1]
            if current.has_children():
                if self._is_last_child_annotated(current):
                    self._annotate_non_terminal(current, frontier)
                else:
                    self._append_children(current, frontier)
            else:
                current.start_position = start
                current.end_position = start.get_next_position(current.value)
                start = Position(current.end_position.line, current.end_position.column)
                frontier.pop()

    def _annotate_non_terminal(self, current, frontier):
        current.start_position = current.value[0].start_position
        current.end_position = current.value[-1].end_position
        frontier.pop()

    def _append_children(self, current, frontier):
        length = len(current.value)
        for i in range(0, length):
            child = current.value[length - i - 1]
            child.parent = current
            frontier.append(child)

    def _is_last_child_annotated(self, node):
        return node.value[-1].start_position and node.value[-1].end_position


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


class CssLookUp(object):
    @staticmethod
    def is_color_name(s):
        return s.lower() in CssLookUp._color_names

    @staticmethod
    def is_heading(s):
        return s in CssLookUp._heading_names

    _heading_names = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    _color_names = ["aliceblue",
                   "antiquewhite",
                   "aqua",
                   "aquamarine",
                   "azure",
                   "beige",
                   "bisque",
                   "black",
                   "blanchedalmond",
                   "blue",
                   "blueviolet",
                   "brown",
                   "burlywood",
                   "cadetblue",
                   "chartreuse",
                   "chocolate",
                   "coral",
                   "cornflowerblue",
                   "cornsilk",
                   "crimson",
                   "cyan",
                   "darkblue",
                   "darkcyan",
                   "darkgoldenrod",
                   "darkgray",
                   "darkgreen",
                   "darkkhaki",
                   "darkmagenta",
                   "darkolivegreen",
                   "darkorange",
                   "darkorchid",
                   "darkred",
                   "darksalmon",
                   "darkseagreen",
                   "darkslateblue",
                   "darkslategray",
                   "darkturquoise",
                   "darkviolet",
                   "deeppink",
                   "deepskyblue",
                   "dimgray",
                   "dodgerblue",
                   "firebrick",
                   "floralwhite",
                   "forestgreen",
                   "fuchsia",
                   "gainsboro",
                   "ghostwhite",
                   "gold",
                   "goldenrod",
                   "gray",
                   "green",
                   "greenyellow",
                   "honeydew",
                   "hotpink",
                   "indianred",
                   "indigo",
                   "ivory",
                   "khaki",
                   "lavender",
                   "lavenderblush",
                   "lawngreen",
                   "lemonchiffon",
                   "lightblue",
                   "lightcoral",
                   "lightcyan",
                   "lightgoldenrodyellow",
                   "lightgray",
                   "lightgreen",
                   "lightpink",
                   "lightsalmon",
                   "lightseagreen",
                   "lightskyblue",
                   "lightslategray",
                   "lightsteelblue",
                   "lightyellow",
                   "lime",
                   "limegreen",
                   "linen",
                   "magenta",
                   "maroon",
                   "mediumaquamarine",
                   "mediumblue",
                   "mediumorchid",
                   "mediumpurple",
                   "mediumseagreen",
                   "mediumslateblue",
                   "mediumspringgreen",
                   "mediumturquoise",
                   "mediumvioletred",
                   "midnightblue",
                   "mintcream",
                   "mistyrose",
                   "moccasin",
                   "navajowhite",
                   "navy",
                   "oldlace",
                   "olive",
                   "olivedrab",
                   "orange",
                   "orangered",
                   "orchid",
                   "palegoldenrod",
                   "palegreen",
                   "paleturquoise",
                   "palevioletred",
                   "papayawhip",
                   "peachpuff",
                   "peru",
                   "pink",
                   "plum",
                   "powderblue",
                   "purple",
                   "rebeccapurple",
                   "red",
                   "rosybrown",
                   "royalblue",
                   "saddlebrown",
                   "salmon",
                   "sandybrown",
                   "seagreen",
                   "seashell",
                   "sienna",
                   "silver",
                   "skyblue",
                   "slateblue",
                   "slategray",
                   "snow",
                   "springgreen",
                   "steelblue",
                   "tan",
                   "teal",
                   "thistle",
                   "tomato",
                   "turquoise",
                   "violet",
                   "wheat",
                   "white",
                   "whitesmoke",
                   "yellow",
                   "yellowgreen"]