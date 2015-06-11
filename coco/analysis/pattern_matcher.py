import coco.ast.ast as ast
import coco.analysis.expressions as expr
import coco.visitor_decorator as vis
import itertools


class Filter():
    def __init__(self, sequences):
        self._sequences = sequences

    def apply(self, nodes):
        result = []
        for index in range(0, len(nodes)):
            node = nodes[index]
            is_filtered, seq_len = self._is_start_if_sequence(node)
            if is_filtered:
                index += seq_len - 1
            else:
                result.append(node)
        return result

    def _is_start_if_sequence(self, node):
        for seq in self._sequences:
            is_filtered, rem_nodes = WhitespaceVariationMatcher.DEFAULT.is_start_of_sequence(seq, node)
            if is_filtered:
                return True, len(seq.all_descs)
        return False, None


Filter.EMPTY = Filter([])


class TreeWalker(object):

    @staticmethod
    def traverse_current_and_descendants(node):
        yield node
        if node.has_children():
            for child in node.value:
                yield from TreeWalker.traverse_current_and_descendants(child)

    @staticmethod
    def traverse_descendants(node):
        if node.has_children():
            for child in node.value:
                yield child
                yield from TreeWalker.traverse_descendants(child)

    @staticmethod
    def traverse_children(node):
        if node.has_children():
            for child in node.value:
                yield child

    @staticmethod
    def get_next_siblings_including(node):
        if not node.parent:
            return [node]
        return node.parent.value[node.index:]

    @staticmethod
    def get_next_siblings_excluding(node):
        if not node.parent:
            return []
        return node.parent.value[node.index+1:]

    @staticmethod
    def get_previous_siblings_including(node):
        if not node.parent:
            return [node]
        return node.parent.value[0:node.index+1]

    @staticmethod
    def get_previous_siblings_excluding(node):
        if not node.parent:
            return []
        return node.parent.value[0:node.index]

    @staticmethod
    def get_siblings_between(node1, node2):
        assert node1.index < node2.index
        assert node1.parent is node2.parent
        start = node1.index + 1
        end = node2.index
        return node1.parent.value[start:end]


class Matcher(object):
    def __init__(self, filter_):
        self._filter = filter_

    def _is_node_desc_match(self, desc, node):
        context = expr.ExprContext(self, node)
        result = expr.ExprEvaluator.evaluate(desc.attr_expr, context)
        return result.value


class WhitespaceVariationMatcher(Matcher):
    def __init__(self, filter_):
        super(WhitespaceVariationMatcher, self).__init__(filter_)

    def is_variation_before_node(self, variation, node):
        """
        Checks whether any of the given sequences appears before the given node. Filter is applied.
        Returns boolean
        """
        prev_siblings = self._filter.apply(TreeWalker.get_previous_siblings_excluding(node))
        for i in range(0, len(prev_siblings)):
            rem_nodes = prev_siblings[i:]
            if self._is_variation_exact_nodes_match(variation, rem_nodes):
                return True
        return False

    def is_variation_after_node(self, variation, node):
        """
        Checks if a variation appears after a given node. Filter is applied.
        Returns boolean
        """
        next_siblings = self._filter.apply(TreeWalker.get_next_siblings_excluding(node))
        return self.is_start_of_variation(variation, next_siblings[0])

    def is_variation_between_nodes(self, variation, node1, node2):
        """
        Checks whether the inner siblings of two nodes match a variation. Filter is applied.
        Returns boolean
        """
        inner_siblings = self._filter.apply(TreeWalker.get_siblings_between(node1, node2))
        return self._is_variation_exact_nodes_match(variation, inner_siblings)

    def is_start_of_variation(self, variation, node):
        """
        The method checks whether a variation of sequences starts from a given node
        Returns boolean
        """
        for s in variation.sequences:
            if self.is_start_of_sequence(s, node):
                return True
        return False

    def is_start_of_sequence(self, sequence, node):
        """
        The method checks whether a sequence exists starting from a given node. No filter applied.
        Returns boolean
        """
        nodes = TreeWalker.get_next_siblings_including(node)
        is_match, rem_nodes = self._get_match_and_remainder(sequence.root_desc, nodes)
        if not is_match:
            return False, None
        rem_desc = self._get_remaining_desc(sequence.all_descs, sequence.root_desc)
        if not rem_desc:
            return True, rem_nodes
        return self.is_start_of_sequence(ast.SequencePatternExpr(rem_desc), rem_nodes[0])

    def _get_remaining_desc(self, all_desc, desc):
        return [i for i in all_desc if i not in [desc]]

    def _is_variation_exact_nodes_match(self, variation, nodes):
        """
        Checks whether a the given nodes match exactly a given variation
        Returns boolean
        """
        for s in variation.sequences:
            if self._is_sequence_exact_nodes_match(s, nodes):
                return True
        return False

    def _is_sequence_exact_nodes_match(self, sequence, nodes):
        """
        The method checks whether the given nodes match exactly the given sequence
        Returns boolean
        """
        is_match, rem_nodes = self._get_match_and_remainder(sequence.root_desc, nodes)
        if not is_match:
            return False
        rem_desc = [item for item in sequence.all_descs if item not in [sequence.root_desc]]
        if not rem_desc:
            return not rem_nodes
        s = ast.SequencePatternExpr(rem_desc)
        return self._is_sequence_exact_nodes_match(s, rem_nodes)

    @vis.visitor(ast.NodeExprWrapper)
    def _get_match_and_remainder(self, desc, nodes):
        """
        Checks if a node descriptor matches a nodes
        Returns boolean if the match occurred and the remaining unmatched nodes
        """
        assert len(nodes) > 0
        if self._is_node_desc_match(desc, nodes[0]):
            return True, nodes[1:]
        return False, nodes

    @vis.visitor(ast.NodeSequenceExprWrapper)
    def _get_match_and_remainder(self, desc, nodes):
        """
        A node descriptor greedily matches a sequence of nodes
        Returns a boolean if the match occurred and the remaining unmatched nodes
        """
        if desc.repeater.is_exact():
            return self._is_lower_matched(desc, nodes)
        return self._handle_range(desc, nodes)

    def _is_lower_matched(self, desc, nodes):
        if len(nodes) < desc.repeater.lower:
            return False, None
        for i in range(0, desc.repeater.lower):
            if not self._is_node_desc_match(desc, nodes[i]):
                return False, None
        return True, nodes[desc.repeater.lower:]

    def _handle_range(self, desc, nodes):
        is_min, rem_nodes = self._is_lower_matched(desc, nodes)
        if is_min:
            _, rem_nodes = self._get_repetitions(desc, rem_nodes)
            return True, rem_nodes
        return False, None

    def _get_repetitions(self, desc, nodes):
        for i, node in enumerate(nodes):
            if not self._is_node_desc_match(desc, node) or not desc.repeater.is_in_range(i):
                return i, nodes[i:]
        return len(nodes), []


WhitespaceVariationMatcher.DEFAULT = WhitespaceVariationMatcher(Filter.EMPTY)


class PatternMatcher(Matcher):
    def __init__(self, filter_):
        super(PatternMatcher, self).__init__(filter_)

    def find_pattern_in_tree(self, tree, pattern):
        """
        The method searches a tree for occurrences of a given pattern
        Returns a list of {desc: node} dictionaries
        """
        result = []
        current_result = {}
        nodes = self._filter_by(tree, pattern.root_desc, TreeWalker.traverse_current_and_descendants)
        return self._process_nodes(nodes, pattern.root_desc, pattern, current_result, result)

    def _process_nodes(self, nodes, desc, pattern, current_result, result):
        for node in nodes:
            self._register_node_match(current_result, desc, node)

            relations = pattern.get_node_relations(desc)
            if self._is_anchor_element(relations):
                result.append(current_result.copy())
            if self._has_single_relation(relations):
                target_desc, new_nodes = self._process_relation(pattern, desc, node)
                return self._process_nodes(new_nodes, target_desc, pattern, current_result, result)
            if self._has_multiple_relations(relations):
                self._process_fork(node, relations, desc, pattern, current_result, result)

            self._unregister_node_match(current_result, desc)
        return result

    def _process_relation(self, pattern_expr, desc, node):
        relation = pattern_expr.get_node_relations(desc)[0]
        nodes = self._find_target_nodes(relation, node)
        return relation.target_node, nodes

    def _process_fork(self, node, relations, desc, pattern, current_result, result):
        target_desc, descendants = self._process_relation(pattern, desc, node)
        for combination in itertools.combinations(descendants, len(relations)):
            self._register_multi_node_match(current_result, relations, combination)
            result.append(current_result.copy())
            self._unregister_multi_node_match(current_result, relations)

    def find_descendants_that_match(self, node, desc):
        """
        Returns a list of all descendant nodes of a given node that match a particular descriptor
        """
        return self._filter_by(node, desc, TreeWalker.traverse_descendants)

    def find_children_that_match(self, node, desc):
        """
        Returns a list of all immediate child nodes of a given node that match a particular descriptor
        """
        return self._filter_by(node, desc, TreeWalker.traverse_children)

    def _filter_by(self, node, desc, func):
        result = []
        for n in func(node):
            if self._is_node_desc_match(desc, n):
                result.append(n)
        return result

    @vis.visitor(ast.IsParentOfRelation)
    def _find_target_nodes(self, relation, node):
        return self.find_children_that_match(node, relation.target_node)

    @vis.visitor(ast.IsAncestorOfRelation)
    def _find_target_nodes(self, relation, node):
        return self.find_descendants_that_match(node, relation.target_node)

    def _register_node_match(self, result, node_desc, node):
        assert node_desc not in result
        result[node_desc] = node

    def _unregister_node_match(self, result, node_desc):
        assert node_desc in result
        result.pop(node_desc)

    def _register_multi_node_match(self, result, relations, nodes):
        for i, r in enumerate(relations):
            result[r.target_node] = nodes[i]

    def _unregister_multi_node_match(self, result, relations):
        for r in relations:
            result.pop(r.target_node)

    def _is_anchor_element(self, relations):
        return len(relations) == 0

    def _has_single_relation(self, relations):
        return len(relations) == 1

    def _has_multiple_relations(self, relations):
        return len(relations) > 1


PatternMatcher.DEFAULT = PatternMatcher(Filter.EMPTY)