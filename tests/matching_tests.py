from unittest import TestCase

from tests.helpers import ParseTreeConstructor
from tests.helpers import PatternConstructor
import csscoco.css.parse_tree as parse
from csscoco.lang.ast import ast as ast
import csscoco.lang.analysis.pattern_matcher as matching


class WhitespaceMatcher(TestCase):

    def setUp(self):
        self.attr_expr = ast.BooleanExpr.build(True)
        self.node0 = parse.TerminalCssNode('newline', '\n')
        self.node1 = parse.TerminalCssNode('space', ' ')
        self.node2 = parse.TerminalCssNode('tab', '\t')
        self.node3 = parse.TerminalCssNode('indent', '    ')
        self.node4 = parse.TerminalCssNode('comment', '/* Comment */')
        self.nodes = [self.node0, self.node1, self.node2, self.node3, self.node4]
        self.matcher = matching.WhitespaceVariationMatcher(matching.Filter.EMPTY)

    def test_is_lower_matched(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(lower=2, upper=2))
        is_matched, rem_nodes = self.matcher._is_lower_matched(desc, [self.node0, self.node1, self.node2])
        assert is_matched
        assert len(rem_nodes) == 1
        assert rem_nodes[0] == self.node2

    def test_not_is_lower_matched(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(lower=2, upper=2))
        is_matched, rem_nodes = self.matcher._is_lower_matched(desc, [self.node0])
        assert not is_matched

    def test_handle_range_more(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(2, 3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1, self.node2, self.node3])
        assert is_matched
        assert len(rem_nodes) == 1

    def test_handle_range_split(self):
        desc = PatternConstructor.build_seq_desc_type('newline', ast.Repeater(1, 3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node0, self.node1])
        assert is_matched
        assert len(rem_nodes) == 1

    def test_handle_range_less(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(1, 2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [])
        assert not is_matched

    def test_handle_max_less(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(upper=3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0])
        assert is_matched
        assert not rem_nodes

    def test_handle_max_exact(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(upper=3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1, self.node2])
        assert is_matched
        assert not rem_nodes

    def test_handle_max_more(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(upper=3))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1, self.node2, self.node3])
        assert is_matched
        assert len(rem_nodes) == 1
        assert rem_nodes[0] == self.node3

    def test_handle_min_less(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(lower=2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0])
        assert not is_matched

    def test_handle_min_exact(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(lower=2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1])
        assert is_matched
        assert not rem_nodes

    def test_handle_min_split(self):
        desc = PatternConstructor.build_seq_desc_type('newline', ast.Repeater(lower=2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node0, self.node1])
        assert is_matched
        assert len(rem_nodes) == 1

    def test_handle_min_more(self):
        desc = PatternConstructor.build_seq_desc(ast.Repeater(lower=2))
        is_matched, rem_nodes = self.matcher._handle_range(desc, [self.node0, self.node1, self.node3])
        assert is_matched
        assert not rem_nodes

    def test_is_sequence_exact_nodes_match(self):
        node_list = [PatternConstructor.build_node_desc('newline'), PatternConstructor.build_node_desc('space')]
        seq = ast.SequencePattern(node_list)
        is_match = self.matcher._is_sequence_exact_nodes_match(seq, [self.node0, self.node1])
        assert is_match

    def test_is_sequence_exact_nodes_match_more(self):
        node_list = [PatternConstructor.build_node_desc('newline'), PatternConstructor.build_node_desc('space')]
        seq = ast.SequencePattern(node_list)
        is_match = self.matcher._is_sequence_exact_nodes_match(seq, [self.node0, self.node1, self.node1])
        assert not is_match

    def test_is_sequence_exact_nodes_match_multi_one(self):
        rep_node = PatternConstructor.build_seq_desc_type('newline', ast.Repeater(lower=3, upper=3))
        node_list = [rep_node]
        seq = ast.SequencePattern(node_list)
        is_match = self.matcher._is_sequence_exact_nodes_match(seq, [self.node0, self.node0, self.node0])
        assert is_match

    def test_is_sequence_exact_nodes_match_multi_two(self):
        rep_node = PatternConstructor.build_seq_desc_type('newline', ast.Repeater(lower=2, upper=3))
        node_list = [PatternConstructor.build_node_desc('space'), rep_node]
        seq = ast.SequencePattern(node_list)
        is_match = self.matcher._is_sequence_exact_nodes_match(seq, [self.node1, self.node0, self.node0])
        assert is_match

    def test_is_start_of_sequence(self):
        node_list = [PatternConstructor.build_node_desc('newline'), PatternConstructor.build_node_desc('space')]
        seq = ast.SequencePattern(node_list)
        root = ParseTreeConstructor.add_root_to_siblings('newline', 'space', 'space')
        is_match, nodes = self.matcher.is_start_of_sequence(seq, root.value[0])
        assert is_match
        assert len(nodes) == 1

    def test_is_start_of_sequence_not(self):
        node_list = [PatternConstructor.build_node_desc('newline'), PatternConstructor.build_node_desc('space')]
        seq = ast.SequencePattern(node_list)
        root = ParseTreeConstructor.add_root_to_siblings('newline', 'tab', 'space')
        is_match, nodes = self.matcher.is_start_of_sequence(seq, root)
        assert not is_match

    def test_is_start_of_sequence_less(self):
        node_list = [PatternConstructor.build_node_desc('newline'), PatternConstructor.build_node_desc('space')]
        seq = ast.SequencePattern(node_list)
        root = ParseTreeConstructor.add_root_to_siblings('newline')
        is_match, nodes = self.matcher.is_start_of_sequence(seq, root)
        assert not is_match

    def test_is_variation_before_node(self):
        variation = ast.WhitespaceVariation([ast.SequencePattern([PatternConstructor.build_node_desc('newline')])])
        root = ParseTreeConstructor.add_root_to_siblings('newline', 'comment')
        present = self.matcher.is_variation_before_node(variation, root.value[1])
        assert present

    def test_is_variation_after_node(self):
        variation = ast.WhitespaceVariation([ast.SequencePattern([PatternConstructor.build_node_desc('newline')])])
        root = ParseTreeConstructor.add_root_to_siblings('comment', 'newline')
        present = self.matcher.is_variation_after_node(variation, root.value[0])
        assert present

    def test_is_variation_between_nodes(self):
        variation = ast.WhitespaceVariation([
            ast.SequencePattern([PatternConstructor.build_node_desc('newline')]),
            ast.SequencePattern([PatternConstructor.build_node_desc('space'), PatternConstructor.build_node_desc('newline')])])
        root = ParseTreeConstructor.add_root_to_siblings('comment', 'newline', 'comment')
        present = self.matcher.is_variation_between_nodes(variation, root.value[0], root.value[2])
        assert present

        root = ParseTreeConstructor.add_root_to_siblings('comment', 'space', 'newline', 'comment')
        present = self.matcher.is_variation_between_nodes(variation, root.value[0], root.value[3])
        assert present


class HierarchicalMatcher(TestCase):

    def setUp(self):
        self.matcher = matching.PatternMatcher(matching.Filter.EMPTY)
        self.tree = ParseTreeConstructor.add_root_to_siblings('ruleset', 'newline')
        ParseTreeConstructor.add_children_to_node('declaration', 'newline', 'declaration', 'space', 'declaration',
                                                  node=self.tree.value[0])
        pass

    def test_find_single_pattern_in_children(self):
        pattern = PatternConstructor.single_node('declaration')
        result = self.matcher.find_pattern_in_tree(self.tree, pattern)
        assert len(result) == 3

    def test_find_single_pattern_in_descendants(self):
        pattern = PatternConstructor.single_node('declaration')
        result = self.matcher.find_pattern_in_tree(self.tree, pattern)
        assert len(result) == 3

    def test_find_parent_child_pattern(self):
        parent = PatternConstructor.build_node_desc('root')
        child = PatternConstructor.build_node_desc('ruleset')
        relations = ast.NodeRelations()
        relations.register_relation(parent, ast.IsParentOf(child))
        pattern = ast.PatternDescriptor(parent, [parent, child], relations)

        result = self.matcher.find_pattern_in_tree(self.tree, pattern)
        assert len(result) == 1

    def test_find_parent_child_pattern_ancestor(self):
        parent = PatternConstructor.build_node_desc('root')
        child = PatternConstructor.build_node_desc('newline')
        relations = ast.NodeRelations()
        relations.register_relation(parent, ast.IsAncestorOf(child))
        pattern = ast.PatternDescriptor(parent, [parent, child], relations)

        result = self.matcher.find_pattern_in_tree(self.tree, pattern)
        assert len(result) == 2

    def test_find_double_pattern(self):
        parent = PatternConstructor.build_node_desc('ruleset')
        child1 = PatternConstructor.build_node_desc('declaration')
        child2 = PatternConstructor.build_node_desc('declaration')
        relations = ast.NodeRelations()
        relations.register_relation(parent, ast.IsParentOf(child1))
        relations.register_relation(parent, ast.IsParentOf(child2))
        pattern = ast.PatternDescriptor(parent, [parent, child1, child2], relations)

        result = self.matcher.find_pattern_in_tree(self.tree, pattern)
        assert len(result) == 3

    def test_find_fork_pattern(self):
        root = PatternConstructor.build_node_desc('root')
        parent = PatternConstructor.build_node_desc('ruleset')
        child1 = PatternConstructor.build_node_desc('declaration')
        child2 = PatternConstructor.build_node_desc('declaration')
        child3 = PatternConstructor.build_node_desc('declaration')
        relations = ast.NodeRelations()
        relations.register_relation(root, ast.IsParentOf(parent))
        relations.register_relation(parent, ast.IsParentOf(child1))
        relations.register_relation(parent, ast.IsParentOf(child2))
        relations.register_relation(parent, ast.IsParentOf(child3))
        pattern = ast.PatternDescriptor(root, [root, parent, child1, child2, child3], relations)

        result = self.matcher.find_pattern_in_tree(self.tree, pattern)
        assert len(result) == 1
