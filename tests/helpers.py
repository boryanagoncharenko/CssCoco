import coco.ast.ast as ast
import css.parse_tree as parse


class ParseTreeConstructor(object):

    @staticmethod
    def add_root_to_siblings(*type_list):
        nodes = ParseTreeConstructor._create_nodes(*type_list)
        root = parse.Node('root', nodes)
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
            nodes.append(parse.Node(type_, ''))
        return nodes

    @staticmethod
    def _annotate_children(node):
        for i, child in enumerate(node.value):
            child.index = i
            child.parent = node


class PatternConstructor(object):

    @staticmethod
    def build_node_desc(type_):
        return ast.NodeExprWrapper(ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string=type_)))

    @staticmethod
    def build_seq_desc(repeater):
        return ast.NodeSequenceExprWrapper(ast.BooleanExpr.TRUE, repeater)

    @staticmethod
    def build_seq_desc_type(type_, repeater):
        return ast.NodeSequenceExprWrapper(
            ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string=type_)), repeater)

    @staticmethod
    def single_node(type_):
        node_expr = PatternConstructor.build_node_desc(type_)
        return ast.PatternExpr(node_expr, [node_expr], ast.Relations())

    @staticmethod
    def parent_child_nodes(parent_type, child_type, relation_type):
        is_parent = ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string=parent_type))
        is_child = ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string=child_type))
        parent = ast.NodeExprWrapper(is_parent)
        child = ast.NodeExprWrapper(is_child)
        relations = ast.Relations()
        if relation_type == 'parent':
            relations.register_relation(parent, ast.IsParentOfRelation(child))
        if relation_type == 'ancestor':
            relations.register_relation(parent, ast.IsAncestorOfRelation(child))
        return ast.PatternExpr(parent, [parent, child], relations)