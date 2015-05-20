

class Sequence(object):
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
        assert self is not Sequence.NONE
        assert sequence is not Sequence.NONE
        if len(sequence) < len(self):
            return False

        for i in range(0, len(sequence)):
            for j in range(0, len(self)):
                if self[j] != sequence[i+j]:
                    break
                if j == len(self) - 1:
                    return True
        return False


Sequence.NONE = Sequence([])


class SequenceVariation(object):

    def __init__(self, sequences, ignore_desc):
        self.sequences = sequences
        self.ignore_desc = ignore_desc

    def __iter__(self):
        return iter(self.sequences)

    def to_error_string(self):
        res = ''
        for s in self.sequences:
            res = ''.join([res, ' or \'', s.to_error_string(), '\''])
        return res[4:]

    def is_part_of_variation(self, variation):
        for os in variation:
            for ms in self.sequences:
                if ms.is_part_of_sequence(os):
                    return True
        return False


SequenceVariation.NONE = SequenceVariation([], None)


class SequenceFinder(object):
    """
    The class is responsible for finding NodeSequences and SequenceOptions in a tree
    """
    @staticmethod
    def find_variation(tree, variation):
        for sequence in variation:
            yield from SequenceFinder._find_sequence(tree, sequence, variation.ignore_desc)

    @staticmethod
    def _find_sequence(tree, sequence, ignore_desc):
        """
        Traverses a tree and returns all occurrences of a given sequence
        """
        if not sequence.is_empty():
            for start in SequenceFinder.find_node_in_tree(tree, sequence[0]):
                success, nodes = SequenceFinder._is_sequence_present_from(start, sequence, ignore_desc)
                if success:
                    yield nodes

    @staticmethod
    def find_node_in_tree(node, desc):
        """
        Returns all nodes that match a given pattern
        """
        if desc.is_match(node):
            yield node
        if node.has_children():
            for child in node.value:
                yield from SequenceFinder.find_node_in_tree(child, desc)

    @staticmethod
    def _is_sequence_present_from(node, sequence, ignore_desc):
        if sequence is Sequence.NONE:
            return False, None
        result = []
        current = node
        for desc in sequence:
            if not current or not desc.is_match(current):
                return False, None
            result.append(current)
            _, current = SequenceFinder._get_next_non_ignored_child(current, ignore_desc)
        return True, result

    @staticmethod
    def _get_next_non_ignored_child(node, ignore_desc):
        parent = node.parent
        if not parent:
            return False, None
        next_child_index = node.index + 1
        number_of_children = len(parent.value)

        for i in range(next_child_index, number_of_children):
            child = parent.value[i]
            if not ignore_desc.is_match(child):
                return True, child
        return False, None


