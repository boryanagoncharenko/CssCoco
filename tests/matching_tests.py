import src.parse_tree as parse
import coco.ast.ast as ast
import coco.analysis.pattern_matcher as matching
from unittest import TestCase


class WhitespaceMatcher(TestCase):

    def setUp(self):
        self.attr_expr = ast.BooleanExpr.build(True)
        self.node0 = parse.TerminalNode('newline', '\n')
        self.node1 = parse.TerminalNode('space', ' ')
        self.node2 = parse.TerminalNode('tab', '\t')
        self.node3 = parse.TerminalNode('indent', '    ')
        self.node4 = parse.TerminalNode('comment', '/* Comment */')
        self.nodes = [self.node0, self.node1, self.node2, self.node3, self.node4]
        self.matcher = matching.WhitespaceVariationMatcher(matching.Filter.EMPTY)

    def get_desc(self, type_):
        return ast.NodeExprWrapper(ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string=type_)))

    def get_seq_desc(self, repeater):
        return ast.NodeSequenceExprWrapper(self.attr_expr, repeater)

    def get_seq_desc_(self, type_, repeater):
        return ast.NodeSequenceExprWrapper(
            ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string=type_)), repeater)

    def construct_tree(self, *type_list):
        nodes = []
        for i, type_ in enumerate(type_list):
            nodes.append(parse.TerminalNode(type_, '    '))
        root = parse.Node('root', nodes)
        for i, child in enumerate(root.value):
            child.index = i
            child.parent = root
        return root

    def test_is_lower_matched(self):
        desc = self.get_seq_desc(ast.Repeater(lower=2, upper=2))
        is_matched, rem_nodes = self.matcher._is_lower_matched(desc, [self.node0, self.node1, self.node2])
        assert is_matched
        assert len(rem_nodes) == 1
        assert rem_nodes[0] == self.node2

    def test_not_is_lower_matched(self):
        desc = self.get_seq_desc(ast.Repeater(lower=2, upper=2))
        is_matched, rem_nodes = self.matcher._is_lower_matched(desc, [self.node0])
        assert not is_matched

    def test_handle_range_more(self):
        desc = self.get_seq_desc(ast.Repeater(2, 3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1, self.node2, self.node3])
        assert is_matched
        assert len(rem_nodes) == 1

    def test_handle_range_split(self):
        desc = self.get_seq_desc_('newline', ast.Repeater(1, 3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node0, self.node1])
        assert is_matched
        assert len(rem_nodes) == 1

    def test_handle_range_less(self):
        desc = self.get_seq_desc(ast.Repeater(1, 2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [])
        assert not is_matched

    def test_handle_max_less(self):
        desc = self.get_seq_desc(ast.Repeater(upper=3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0])
        assert is_matched
        assert not rem_nodes

    def test_handle_max_exact(self):
        desc = self.get_seq_desc(ast.Repeater(upper=3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1, self.node2])
        assert is_matched
        assert not rem_nodes

    def test_handle_max_more(self):
        desc = self.get_seq_desc(ast.Repeater(upper=3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1, self.node2, self.node3])
        assert is_matched
        assert len(rem_nodes) == 1
        assert rem_nodes[0] == self.node3

    def test_handle_min_less(self):
        desc = self.get_seq_desc(ast.Repeater(lower=2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0])
        assert not is_matched

    def test_handle_min_exact(self):
        desc = self.get_seq_desc(ast.Repeater(lower=2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1])
        assert is_matched
        assert not rem_nodes

    def test_handle_min_split(self):
        desc = self.get_seq_desc_('newline', ast.Repeater(lower=2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node0, self.node1])
        assert is_matched
        assert len(rem_nodes) == 1

    def test_handle_min_more(self):
        desc = self.get_seq_desc(ast.Repeater(lower=2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1, self.node3])
        assert is_matched
        assert not rem_nodes

    def test_is_sequence_exact_nodes_match(self):
        node_list = [self.get_desc('newline'), self.get_desc('space')]
        seq = ast.SequencePatternExpr(node_list)
        is_match = self.matcher._is_sequence_exact_nodes_match(seq, [self.node0, self.node1])
        assert is_match

    def test_is_sequence_exact_nodes_match_more(self):
        node_list = [self.get_desc('newline'), self.get_desc('space')]
        seq = ast.SequencePatternExpr(node_list)
        is_match = self.matcher._is_sequence_exact_nodes_match(seq, [self.node0, self.node1, self.node1])
        assert not is_match

    def test_is_sequence_exact_nodes_match_multi_one(self):
        rep_node = self.get_seq_desc_('newline', ast.Repeater(lower=3, upper=3))
        node_list = [rep_node]
        seq = ast.SequencePatternExpr(node_list)
        is_match = self.matcher._is_sequence_exact_nodes_match(seq, [self.node0, self.node0, self.node0])
        assert is_match

    def test_is_sequence_exact_nodes_match_multi_two(self):
        rep_node = self.get_seq_desc_('newline', ast.Repeater(lower=2, upper=3))
        node_list = [self.get_desc('space'), rep_node]
        seq = ast.SequencePatternExpr(node_list)
        is_match = self.matcher._is_sequence_exact_nodes_match(seq, [self.node1, self.node0, self.node0])
        assert is_match

    def test_is_start_of_sequence(self):
        node_list = [self.get_desc('newline'), self.get_desc('space')]
        seq = ast.SequencePatternExpr(node_list)
        root = self.construct_tree('newline', 'space', 'space')
        is_match, nodes = self.matcher.is_start_of_sequence(seq, root.value[0])
        assert is_match
        assert len(nodes) == 1

    def test_is_start_of_sequence_not(self):
        node_list = [self.get_desc('newline'), self.get_desc('space')]
        seq = ast.SequencePatternExpr(node_list)
        root = self.construct_tree('newline', 'tab', 'space')
        is_match, nodes = self.matcher.is_start_of_sequence(seq, root)
        assert not is_match

    def test_is_start_of_sequence_less(self):
        node_list = [self.get_desc('newline'), self.get_desc('space')]
        seq = ast.SequencePatternExpr(node_list)
        root = self.construct_tree('newline')
        is_match, nodes = self.matcher.is_start_of_sequence(seq, root)
        assert not is_match

    def test_is_variation_before_node(self):
        variation = ast.WhitespaceVariation([ast.SequencePatternExpr([self.get_desc('newline')])])
        root = self.construct_tree('newline', 'comment')
        present = self.matcher.is_variation_before_node(variation, root.value[1])
        assert present

    def test_is_variation_after_node(self):
        variation = ast.WhitespaceVariation([ast.SequencePatternExpr([self.get_desc('newline')])])
        root = self.construct_tree('comment', 'newline')
        present = self.matcher.is_variation_after_node(variation, root.value[0])
        assert present

    def test_is_variation_between_nodes(self):
        variation = ast.WhitespaceVariation([
            ast.SequencePatternExpr([self.get_desc('newline')]),
            ast.SequencePatternExpr([self.get_desc('space'), self.get_desc('newline')])])
        root = self.construct_tree('comment', 'newline', 'comment')
        present = self.matcher.is_variation_between_nodes(variation, root.value[0], root.value[2])
        assert present

        root = self.construct_tree('comment', 'space', 'newline', 'comment')
        present = self.matcher.is_variation_between_nodes(variation, root.value[0], root.value[3])
        assert present


class HierarchicalMatcher(TestCase):

    def setUp(self):
        pass

    def test_handle_min_more(self):
        pass