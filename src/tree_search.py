import abc


class NodeDescriptor(object):

    @abc.abstractmethod
    def is_match(self, node):
        pass


class SimpleDescriptor(NodeDescriptor):
    """
    Contains information about the type and/or value of a node
    """
    def __init__(self, type_=None, value=None):
        self.type_ = type_
        self.value = value
        self.search_by_type = self.type_ is not None
        self.search_by_value = self.value is not None

    def is_match(self, node):
        """
        Returns a boolean value indicating whether the node matches the descriptor
        """
        return self._match_type(node.type_) and self._match_value(node.value)

    def _match_value(self, node_value):
        if self.search_by_value:
            return self.value == node_value
        return True

    def _match_type(self, node_type):
        if self.search_by_type:
            return self.type_ == node_type
        return True

    def get_type_and_value_str(self):
        type_str = (' type=' + self.type_) if self.search_by_type else ''
        value_str = (' value=' + self.value) if self.search_by_value else ''
        return type_str, value_str

    def __str__(self):
        type_str, value_str = self.get_type_and_value_str()
        return ''.join([' Simple Descriptor:', type_str, value_str])


class CompoundDescriptor(NodeDescriptor):
    """
    Contains a list of SimpleDescriptors and tries to match with any of them
    """
    def __init__(self, descriptors):
        self.descriptors = descriptors

    def is_match(self, node):
        """
        Returns a boolean value indicating whether the node matches any of the descriptors
        """
        for d in self.descriptors:
            if d.is_match(node):
                return True
        return False

    def __str__(self):
        s = ''
        for d in self.descriptors:
            type_str, value_str = d.get_type_and_value_str()
            s = ''.join([s, ' ', type_str, ' ', value_str, ' or'])
        return ''.join([' Compound Descriptor:', s[:-2]])


NodeDescriptor.ANY = NodeDescriptor()

CompoundDescriptor.WHITESPACE = CompoundDescriptor([SimpleDescriptor(type_='space'),
                                                    SimpleDescriptor(type_='indent'),
                                                    SimpleDescriptor(type_='tab'),
                                                    SimpleDescriptor(type_='newline')])

CompoundDescriptor.INDENT = CompoundDescriptor([SimpleDescriptor(type_='indent')])


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


Sequence.NONE = Sequence([])


class SequenceVariation(object):

    def __init__(self, sequences, ignore_desc):
        self.sequences = sequences
        self.ignore_desc = ignore_desc

    def __iter__(self):
        return iter(self.sequences)

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
    def is_option_present_after(node, option):
        if option is SequenceVariation.NONE:
            return True

        for sequence in option:
            if SequenceFinder._is_sequence_present_after(node, sequence, option.ignore_desc):
                return True
        return False

    @staticmethod
    def _is_sequence_present_after(node, sequence, ignore_desc=None):
        if sequence is not Sequence.NONE:
            ignore_desc = sequence.ignore_desc if ignore_desc is None else ignore_desc
            current_node = node
            for desc in sequence:
                is_valid, next_node = SequenceFinder._get_next_non_ignored_child(current_node, ignore_desc)
                if not is_valid or not desc.is_match(next_node):
                    return False
                current_node = next_node
        return True

    @staticmethod
    def is_option_present_before(node, option):
        if option is SequenceVariation.NONE:
            return True

        for sequence in option:
            if SequenceFinder._is_sequence_present_before(node, sequence, ignore_desc=option.ignore_desc):
                return True
        return False

    @staticmethod
    def _is_sequence_present_before(node, sequence, ignore_desc=None):
        if sequence is not Sequence.NONE:
            ignore_desc = sequence.ignore_desc if ignore_desc is None else ignore_desc
            nodes_before = SequenceFinder._get_n_non_ignored_before(len(sequence), node, ignore_desc)
            if not nodes_before:
                return False
            for index, node_before in enumerate(nodes_before):
                if not sequence[index].is_match(node_before):
                    return False
        return True

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
        next_child_index = node.index + 1
        number_of_children = len(parent.value)

        for i in range(next_child_index, number_of_children):
            child = parent.value[i]
            if not ignore_desc.is_match(child):
                return True, child

        return False, None

    @staticmethod
    def _get_n_non_ignored_before(n, node, ignore_desc):
        parent = node.parent
        result = []
        for i in range(0, node.index):
            child = parent.value[i]
            if not ignore_desc.is_match(child):
                result.append(child)
        return result[-n:]


class Requirement(object):
    """
    Describes how the whitespaces around the css nodes should be
    Requires n+1 whitespace variations to be provided for n css nodes: before, inner and after nodes
    """
    def __init__(self, variation_list, ignore_desc=None):
        self.variation_list = variation_list
        self.ignore_desc = ignore_desc

    def is_fulfilled(self, nodes):
        assert len(nodes) > 0
        first_child = nodes[0]
        return self._is_before_fulfilled(first_child) and \
            self._are_inner_and_after_fulfilled(nodes)

    def _are_inner_and_after_fulfilled(self, nodes):
        if len(self.variation_list) < 2:
            return True
        inner_and_after_options = self.variation_list[1:]
        for index, option in enumerate(inner_and_after_options):
            node = nodes[index]
            if not SequenceFinder.is_option_present_after(node, option):
                return False
        return True

    def _is_before_fulfilled(self, first_child_index):
        if len(self.variation_list) < 2:
            return True
        before_option = self.variation_list[0]
        return SequenceFinder.is_option_present_before(first_child_index, before_option)


class Convention(object):

    @abc.abstractmethod
    def is_violated(self, tree):
        pass


class IfThenConvention(Convention):

    def __init__(self, cond_variation, requirement):
        self._cond_variation = cond_variation
        self._requirement = requirement

    def is_violated(self, tree):
        for nodes in SequenceFinder.find_variation(tree, self._cond_variation):
            print(self._requirement.is_fulfilled(nodes))
        # TODO: return useful information about the result


class ForbidConvention(Convention):

    def __init__(self, variation):
        self.variation = variation

    def is_violated(self, tree):
        for nodes in SequenceFinder.find_variation(tree, self.variation):
            print('Found')


class ConventionsMap(object):

    def __init__(self, conventions):
        self.conventions = conventions

    def __iter__(self):
        return self.conventions.__iter__()
