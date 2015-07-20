from csscoco.lang.ast import ast as ast
import csscoco.css.parse_tree as parse


class ParseTreeConstructor(object):

    @staticmethod
    def add_root_to_siblings(*type_list):
        nodes = ParseTreeConstructor._create_nodes(*type_list)
        root = parse.CssNode('root', nodes)
        ParseTreeConstructor._annotate_children(root)
        return root

    @staticmethod
    def add_children_to_node(*type_list, node):
        nodes = ParseTreeConstructor._create_nodes(*type_list)
        node.value = nodes
        ParseTreeConstructor._annotate_children(node)
        return node

    @staticmethod
    def _create_nodes(*type_list):
        nodes = []
        for i, type_ in enumerate(type_list):
            nodes.append(parse.CssNode(type_, ''))
        return nodes

    @staticmethod
    def _annotate_children(node):
        for i, child in enumerate(node.value):
            child.index = i
            child.parent = node


class PatternConstructor(object):

    @staticmethod
    def build_node_desc(type_):
        return ast.Node(ast.NodeTypeDescriptor(type_=type_))

    @staticmethod
    def build_seq_desc(repeater):
        return ast.WhitespaceNode(ast.NodeTypeDescriptor(), repeater)

    @staticmethod
    def build_seq_desc_type(type_, repeater):
        return ast.WhitespaceNode(ast.NodeTypeDescriptor(type_=type_), repeater)

    @staticmethod
    def single_node(type_):
        node_expr = PatternConstructor.build_node_desc(type_)
        return ast.PatternDescriptor(node_expr, [node_expr], ast.NodeRelations())
