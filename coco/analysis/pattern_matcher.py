import coco.ast.ast as ast
import coco.analysis.expressions as expr
import coco.visitor_decorator as vis
import itertools

# class Filter(object):
#     def __init__(self, sequences):
#         self._sequences = sequences
#
#     def apply(self, node_list):
#         index = 0
#         while index < len(node_list):
#             node = node_list[index]
#             is_sequence, length = self._is_start_of_sequence(node)
#             if is_sequence:
#                 index += length
#             else:
#                 yield node
#                 index += 1
#
#     def _is_start_of_sequence(self, node):
#         for seq in self._sequences:
#             if PatternMatcher.DEFAULT.sequence_exists_from(seq, node):
#                 return True, len(seq.all_descs)
#         return False, -1
#
#
# Filter.EMPTY = Filter([])


class Filter():
    def __init__(self, sequences):
        self._sequences = sequences

    def apply(self, nodes):
        index = 0
        result = []
        while index < len(nodes):
            node = nodes[index]
            is_filtered, seq_len = self._inner_apply_filter(node)
            if is_filtered:
                index += seq_len
            else:
                result.append(node)
                index += 1
        return result

    def _inner_apply_filter(self, node):
        for seq in self._sequences:
            is_filtered, rem_nodes = WhitespaceVariationMatcher.DEFAULT.is_sequence_start(seq, node)
            if is_filtered:
                return True, len(seq.all_descs)
        return False, None


Filter.EMPTY = Filter([])

class SequencePatternMatcher(object):

    def sequence_starts_at(self, filter, sequence):
        pass

    def sequence_matches_nodes_exactly(self, nodes_list, sequence):
        pass

    def sequence_appears_before(self, filter, sequence):
        pass


class HierarchicalPatternMatcher(object):

    def find_node_in_tree(self, filter, desc):
        # traverse the tree and find the occurrences of a single node
        pass

    def find_pattern_in_tree(self, filter, pattern):
        # find root nodes using find_node_in_tree
        # use does pattern exist from node
        pass

    def _pattern_starts_at_node(self, filter, pattern):
        pass

    def find_descendant(self, filter, desc):
        pass

    def find_all(self, filter, desc):
        pass

    def produce_combinations(self):
        pass


class PatternFinder(object):
    # Searches for patterns and returns a {desc: node} dictionary
    pass


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
    def get_nodes_between(node1, node2):
        assert node1.index < node2.index
        assert node1.parent is node2.parent
        start = node1.index + 1
        end = node2.index
        return node1.parent[start:end]


class WhitespaceVariationMatcher(object):
    def __init__(self, filter_):
        self._filter = filter_

    def _get_btw_nodes(self, node1, node2):
        nodes = TreeWalker.get_nodes_between(node1, node2)
        return self._filter.apply(nodes)

    def is_sequence_start(self, sequence, node):
        """
        The method checks whether a sequence exists starting from a given node
        Returns a boolean
        """
        nodes = TreeWalker.get_next_siblings_including(node)
        is_match, rem_nodes = self._is_match(sequence.root_desc, nodes)
        if not is_match:
            return False, None
        rem_desc = [item for item in sequence.all_descs if item not in [sequence.root_desc]]
        if not rem_desc:
            return True, rem_desc
        s = ast.SequencePatternExpr(rem_desc)
        return self.is_sequence_start(s, rem_nodes[0])

    def is_variation_before_node(self, variation, node):
        parent = node.parent
        if not parent:
            return False
        filtered_nodes_before = self._filter.apply(TreeWalker.get_previous_siblings_excluding(node))
        for i in range(0, len(filtered_nodes_before)):
            rem_nodes = filtered_nodes_before[i:]
            for s in variation.sequences:
                if self.is_sequence_exact_nodes_match(s, rem_nodes):
                    return True
        return False

    def is_variation_after_node(self, variation, node):
        parent = node.parent
        if not parent:
            return False
        filtered_nodes_after = self._filter.apply(parent.value[node.index:])
        if not filtered_nodes_after:
            return False
        for s in variation.sequences:
            if self.is_sequence_start(s, filtered_nodes_after[0]):
                return True
        return False

    def is_variation_between_nodes(self, variation, node1, node2):
        for sequence in variation.sequences:
            if self.is_sequence_exact_nodes_match(sequence, self._get_btw_nodes(node1, node2)):
                return True
        return False

    def is_sequence_exact_nodes_match(self, sequence, nodes):
        """
        The method checks whether the given nodes match exactly the given sequence
        Returns a boolean
        """
        is_match, rem_nodes = self._is_match(sequence.root_desc, nodes)
        if not is_match:
            return False
        rem_desc = [item for item in sequence.all_descs if item not in [sequence.root_desc]]
        if not rem_desc:
            return not rem_nodes
        s = ast.SequencePatternExpr(rem_desc)
        return self.is_sequence_exact_nodes_match(s, rem_nodes)

    def _does_desc_select_node(self, desc, node):
        context = expr.ExprContext(self, node)
        result = expr.ExprEvaluator.evaluate(desc.attr_expr, context)
        return result.value

    @vis.visitor(ast.NodeExprWrapper)
    def _is_match(self, desc, nodes):
        assert len(nodes) > 0
        if self._does_desc_select_node(desc, nodes[0]):
            return True, nodes[1:]
        return False, nodes

    @vis.visitor(ast.NodeSequenceExprWrapper)
    def _is_match(self, desc, nodes):
        # assert len(nodes) > 0
        if desc.repeater.is_exact():
            return self._hand_exact(desc, nodes)
        if desc.repeater.is_range():
            return self._handle_range(desc, nodes)
        if desc.repeater.is_max():
            return self._handle_max(desc, nodes)
        return self._handle_min(desc, nodes)

    def _hand_exact(self, desc, nodes):
        if len(nodes) < desc.repeater.lower:
            return False, None
        for i in range(0, desc.repeater.lower):
            if not self._does_desc_select_node(desc, nodes[i]):
                return False, None
        return True, nodes[desc.repeater.lower+1:]

    def _handle_range(self, desc, nodes):
        if len(nodes) < desc.repeater.lower:
            return False, None
        is_min, rem_nodes = self._is_min_match(desc, nodes)
        if is_min:
            reps, rem_nodes = self._get_repetitions(desc, rem_nodes)
            if reps <= desc.repeater.upper - desc.repeater.lower:
                return True, rem_nodes
        return False, None

    def _handle_max(self, desc, nodes):
        reps, rem_nodes = self._get_repetitions(desc, nodes)
        if reps < desc.repeater.upper:
            return True, rem_nodes
        return False, None

    def _handle_min(self, desc, nodes):
        is_met, rem_nodes = self._is_min_match(desc, nodes)
        if is_met:
            _, rem_nodes = self._get_repetitions(desc, rem_nodes)
            return True, rem_nodes
        return False, None

    def _is_min_match(self, desc, nodes):
        if len(nodes) < desc.repeater.lower:
            return False, None
        for i in range(0, desc.repeater.lower):
            if not self._does_desc_select_node(desc, nodes[i]):
                return False, None
        return True, nodes[desc.repeater.lower:]

    def _get_repetitions(self, desc, nodes):
        for i, node in enumerate(nodes):
            if not self._does_desc_select_node(desc, node):
                return i, nodes[i+1:]
        return len(nodes), []


WhitespaceVariationMatcher.DEFAULT = WhitespaceVariationMatcher(Filter.EMPTY)


class PatternMatcher(object):
    def __init__(self, filter_seq):
        self.filter_seq = filter_seq

    def is_match(self, desc, node):
        """
        Creates the evaluation context and evaluates whether the node matches the descriptor
        """
        context = expr.ExprContext(self, node)
        result = expr.ExprEvaluator.evaluate(desc.attr_expr, context)
        return result.value

    def find_pattern_occurrences(self, tree, pattern):
        result = []
        current_result = {}
        nodes = self.filter(tree, pattern.root_desc, TreeWalker.traverse_current_and_descendants)
        return self.test(nodes, pattern.root_desc, pattern, current_result, result)

    def test(self, nodes, desc, pattern, current_result, result):
        for node in nodes:
            self.register_match(current_result, desc, node)
            relations = pattern.get_node_relations(desc)

            if self.has_one_descendant(relations):
                target_desc, new_nodes = self.find_related_nodes(pattern, desc, node)
                return self.test(new_nodes, target_desc, pattern, current_result, result)

            if self.has_multiple_descendants(relations):
                self.handle_fork(node, relations, desc, pattern, current_result, result)
            else:
                result.append(current_result.copy())

            self.unregister_match(current_result, desc)
        return result

    def has_one_descendant(self, relations):
        return len(relations) == 1

    def has_multiple_descendants(self, relations):
        return len(relations) > 1

    def find_related_nodes(self, pattern_expr, desc, node):
        relation = pattern_expr.get_node_relations(desc)[0]
        method = self.find_target(relation)
        nodes = method(node, relation.target_node)
        return relation.target_node, nodes

    def handle_fork(self, node, relations, desc, pattern, current_result, result):
        target_desc, descendants = self.find_related_nodes(pattern, desc, node)
        for combination in itertools.combinations(descendants, len(relations)):
            self.register_multi_match(current_result, relations, combination)
            result.append(current_result.copy())
            self.unregister_multi_match(current_result, relations)

    def find_descendant(self, node, desc):
        """
        Returns all nodes that match a given pattern
        """
        if node.has_children():
            for child in self.filter_seq.apply(node.value):
                print(child)
                yield from self._find_in_current_and_descendants(child, desc)

    def find_descendants_that_match(self, node, desc):
        """
        Returns all descendant nodes of a given node that match a particular descriptor
        """
        return self.filter(node, desc, TreeWalker.traverse_descendants)

    def filter(self, node, desc, func):
        result = []
        for n in func(node):
            if self.is_match(desc, n):
                result.append(n)
        return result

    def _find_in_current_and_descendants(self, node, desc):
        if self.is_match(desc, node):
            yield node
        if node.has_children():
            for child in self.filter_seq.apply(node.value):
                yield from self._find_in_current_and_descendants(child, desc)

    def find_next_adjacent_sibling_that_matches(self, node, desc):
        result = []
        siblings = TreeWalker.get_next_siblings_excluding(node)
        filtered = self.filter_seq.apply(siblings)
        if filtered and self.is_match(desc, filtered[0]):
            result.append(filtered[0])
        return result

    def is_anchor(self, pattern_expr, node_desc):
        return not pattern_expr.get_node_relations(node_desc)

    def register_match(self, result, node_desc, node):
        assert node_desc not in result
        result[node_desc] = node

    def unregister_match(self, result, node_desc):
        assert node_desc in result
        result.pop(node_desc)

    def register_multi_match(self, result, relations, nodes):
        for i, r in enumerate(relations):
            result[r.target_node] = nodes[i]

    def unregister_multi_match(self, result, relations):
        for r in relations:
            result.pop(r.target_node)

    @vis.visitor(ast.IsParentOfRelation)
    def find_target(self, relation):
        return self.find_descendants_that_match

    @vis.visitor(ast.IsPreviousSiblingOfRelation)
    def find_target(self, relation):
        return self.find_next_adjacent_sibling_that_matches

PatternMatcher.DEFAULT = PatternMatcher(Filter.EMPTY)