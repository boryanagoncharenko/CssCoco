

class ParentPatternChain(object):
    def __iter__(self, patterns):
        self.patterns = patterns


class ParentPattern(object):

    def is_deep_search(self):
        pass


class DescendantPattern(ParentPattern):
    """
    This pattern is for deep search, e.g. rule >> id
    """
    def __init__(self, parent_desc, child_desc):
        self.parent_desc = parent_desc
        self.child_desc = child_desc

    def is_deep_search(self):
        return True


class ChildPattern(ParentPattern):
    """
    This pattern is for immediate children, block > declaration
    """
    def __init__(self, parent_desc, child_desc):
        self.parent_desc = parent_desc
        self.child_desc = child_desc

    def is_deep_search(self):
        return False


class SiblingSequence(object):
    """
    The class contains a list of descriptors that describe sibling nodes that need to matched
    """
    def __init__(self, descriptors):
        self.descriptors = descriptors

    def __iter__(self):
        return iter(self.descriptors)

    def __getitem__(self, item):
        return self.descriptors[item]

    def is_empty(self):
        return len(self.descriptors) == 0

    def __len__(self):
        return len(self.descriptors)

    def to_error_string(self, to_index=None):
        to_index = len(self.descriptors) if to_index is None else to_index
        s = ''
        for i in range(0, to_index):
            s = ''.join([s, self.descriptors[i].to_error_string()])
        return s

    def is_part_of_sequence(self, sequence):
        assert self is not SiblingSequence.NONE
        assert sequence is not SiblingSequence.NONE
        if len(sequence) < len(self):
            return False

        for i in range(0, len(sequence)):
            for j in range(0, len(self)):
                if self[j] != sequence[i+j]:
                    break
                if j == len(self) - 1:
                    return True
        return False


SiblingSequence.NONE = SiblingSequence([])


class SiblingsVariation(object):

    def __init__(self, match_sequences, ignore_sequences):
        self.match_sequences = match_sequences
        self.ignore_sequences = ignore_sequences

    def __iter__(self):
        return iter(self.match_sequences)

    def to_error_string(self):
        res = ''
        for s in self.match_sequences:
            res = ''.join([res, ' or \'', s.to_error_string(), '\''])
        return res[4:]

    def is_part_of_variation(self, variation):
        for os in variation:
            for ms in self.match_sequences:
                if ms.is_part_of_sequence(os):
                    return True
        return False


SiblingsVariation.NONE = SiblingsVariation([], [])


class TreeWalker(object):

    @staticmethod
    def find_parent_child_pattern(tree, pc_pattern):
        for node in TreeWalker.find_node_in_tree(tree, pc_pattern.parent_desc):
            if node.has_children():
                for child in node.value:
                    if pc_pattern.child_desc.is_match(child):
                        yield [node, child]

    @staticmethod
    def find_variation_in_tree(tree, variation):
        for sequence in variation:
            yield from TreeWalker.find_sequence_in_tree(tree, sequence, variation.ignore_sequences)

    @staticmethod
    def find_sequence_in_tree(tree, sequence, ignore_sequences):
        """
        Traverses a tree and returns all occurrences of a given sequence
        """
        if not sequence.is_empty():
            for node in TreeWalker.find_node_in_tree(tree, sequence[0]):
                next_nodes = node.get_next_siblings_including()
                sieved_nodes = TreeWalker.sieve_non_ignored_nodes(next_nodes, ignore_sequences)
                sieved_nodes = sieved_nodes[:len(sequence)]
                if TreeWalker.is_sequence_exact_match(sequence, sieved_nodes):
                    yield sieved_nodes

    @staticmethod
    def find_node_in_tree(node, desc):
        """
        Returns all nodes that match a given pattern
        """
        if desc.is_match(node):
            yield node
        if node.has_children():
            for child in node.value:
                yield from TreeWalker.find_node_in_tree(child, desc)

    @staticmethod
    def is_sequence_exact_match(sequence, nodes):
        """
        The method returns True if the given nodes match the given sequence.
        No ignoring of nodes is performed
        :param sequence: the sequence that needs to be matched
        :param nodes: the nodes that need to be checked against the sequence
        :return: a boolean value that indicates whether there is a match
        """
        if len(sequence) != len(nodes):
            return False  # There is a mismatch in the length
        for i, desc in enumerate(sequence):
            if not desc.is_match(nodes[i]):
                return False  # There is no match
        return True

    @staticmethod
    def is_variation_exact_match(variation, nodes):
        """
        The method returns True if the given nodes match a sequence in the given variation.
        No ignoring of nodes is performed
        :param variation: the variation that needs to be matched
        :param nodes: the nodes that need to be checked against the variation
        :return: a boolean value indicating if there is a match,
        the sequence that was matched successfully,
        the nodes that matched the sequence
        """
        for sequence in variation:
            is_match = TreeWalker.is_sequence_exact_match(sequence, nodes)
            if is_match:
                return True, sequence, nodes
        return False, SiblingSequence.NONE, nodes

    @staticmethod
    def is_variation_present_btw_two_nodes(variation, node_start, node_end, ignored_sequences):
        assert node_start.parent is node_end.parent
        assert node_start.index < node_end.index
        assert variation is not SiblingsVariation.NONE

        parent = node_start.parent
        if not parent:
            raise NotImplementedError('Y is your parent None?!')
        nodes = parent.value[node_start.index+1:node_end.index]
        nodes = TreeWalker.sieve_non_ignored_nodes(nodes, ignored_sequences)
        return TreeWalker.is_variation_exact_match(variation, nodes)

    @staticmethod
    def sieve_non_ignored_nodes(nodes, ignore_sequences):
        if not nodes:
            return []
        res = []
        i = 0
        while i < len(nodes):
            child = nodes[i]
            is_beginning_of_seq, seq = TreeWalker._sieve_helper(child, ignore_sequences)
            if is_beginning_of_seq:
                i += len(seq)
            else:
                res.append(child)
                i += 1
        return res

    @staticmethod
    def _sieve_helper(node, ignore_sequences):
        for sequence in ignore_sequences:
            if TreeWalker.is_node_beginning_of_sequence(node, sequence):
                return True, sequence
        return False, None

    @staticmethod
    def is_node_beginning_of_sequence(node, sequence):
        if not node.parent:
            return False
        nodes = node.parent.value[node.index:]
        nodes = nodes[:len(sequence)]
        return TreeWalker.is_sequence_exact_match(sequence, nodes)

    @staticmethod
    def get_non_ignored_nodes_before_node(node, cond_ignore_sequences, ignore_sequences):
        from_node = TreeWalker.get_previous_non_ignored_node(node, cond_ignore_sequences)
        if not from_node:
            return []
        nodes = node.parent.value[from_node.index+1:node.index]
        return TreeWalker.sieve_non_ignored_nodes(nodes, ignore_sequences)

    @staticmethod
    def get_previous_non_ignored_node(node, ignore_sequences):
        prev_nodes = node.get_previous_siblings_excluding()
        if not prev_nodes:
            return None
        sieved_nodes = TreeWalker.sieve_non_ignored_nodes(prev_nodes, ignore_sequences)
        if not sieved_nodes:
            return None
        return sieved_nodes[-1]

    @staticmethod
    def get_non_ignored_nodes_after_node(node, cond_ignore_sequences, ignore_sequences):
        after_node = TreeWalker.get_next_non_ignored_node(node, cond_ignore_sequences)
        if not after_node:
            return []
        nodes = node.parent.value[node.index+1:after_node.index]
        return TreeWalker.sieve_non_ignored_nodes(nodes, ignore_sequences)

    @staticmethod
    def get_next_non_ignored_node(node, ignore_sequences):
        next_nodes = node.get_next_siblings_excluding()
        if not next_nodes:
            return None
        sieved_nodes = TreeWalker.sieve_non_ignored_nodes(next_nodes, ignore_sequences)
        if not sieved_nodes:
            return None
        return sieved_nodes[0]

