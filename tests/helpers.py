import antlr4 as antlr4
import json

from csscoco.lang.ast import ast as ast
import csscoco.css.parse_tree as parse
import csscoco.css.parser as css_parser
import csscoco.lang.syntax.ast_builder as builder
import csscoco.lang.syntax.cocoLexer as lexer
import csscoco.lang.syntax.cocoParser as parser


class ParseTreeConstructor(object):

    @staticmethod
    def add_root_to_siblings(*type_list):
        nodes = ParseTreeConstructor._create_nodes(*type_list)
        root = parse.CssNode(nodes, categories=['root'])
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
            nodes.append(parse.CssNode('', categories=[type_]))
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


class ParseHelper(object):

    @staticmethod
    def parse_coco_string(data):
        input_stream = antlr4.FileStream(data)
        l = lexer.cocoLexer(input_stream)
        stream = antlr4.CommonTokenStream(l)
        p = parser.cocoParser(stream)
        tree = p.stylesheet()
        visitor = builder.CocoCustomVisitor()
        convention_set = visitor.visitStylesheet(tree)
        return convention_set

    @staticmethod
    def parse_css_string(css_source):
        result = css_parser.Parser.parse_css(css_source)
        try:
            l = json.loads(result.decode('utf-8'))
        except ValueError:
            raise ValueError()
        tr = css_parser.SExprTransformer.transform(l)
        return parse.ParseTreeBuilder.build(tr)