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

WHITESPACE_DESC = CompoundDescriptor([SimpleDescriptor(type_='space'),
                                      SimpleDescriptor(type_='indent'),
                                      SimpleDescriptor(type_='tab'),
                                      SimpleDescriptor(type_='newline')])


class NodeSequence(object):
    """
    The class contains a list of descriptors that describe sibling nodes that need to matched and
    a descriptor for the nodes that need to be ignored
    """
    def __init__(self, descriptors, ignore_desc):
        self.descriptors = descriptors
        self.ignore_desc = ignore_desc

    def __getitem__(self, item):
        return self.descriptors[item]

    def is_empty(self):
        return len(self.descriptors) == 0

    def __len__(self):
        return len(self.descriptors)

    def __iter__(self):
        return iter(self.descriptors)

NodeSequence.NONE_SEQUENCE = NodeSequence([], None)


class SequenceOption(object):

    def __init__(self, sequences, ignore_desc):
        self.sequences = sequences
        self.ignore_desc = ignore_desc

    def __iter__(self):
        return iter(self.sequences)

SequenceOption.NONE_OPTION = SequenceOption([], None)


class SequenceFinder(object):
    """
    The class is responsible for finding NodeSequences and SequenceOptions in a tree
    """
    @staticmethod
    def find_sequence_option(tree, option):
        for s in option:
            yield from SequenceFinder.find_sequence(tree, s)

    @staticmethod
    def find_sequence(tree, sequence):
        yield from Walker().find_pattern(tree, sequence)

    @staticmethod
    def find_node(tree, node_desc):
        """
        Traverses a tree and yields all nodes that match a given descriptor
        """
        if node_desc.is_match(tree):
            yield tree
        if tree.has_children():
            for child in tree.value:
                yield from SequenceFinder.find_node(child, node_desc)

    @staticmethod
    def is_option_present_after(node, option):
        if option is SequenceOption.NONE_OPTION:
            return True

        for sequence in option:
            if SequenceFinder.is_sequence_present_after(node, sequence, option.ignore_desc):
                return True
        return False

    @staticmethod
    def is_sequence_present_after(node, sequence, ignore_desc=None):
        if sequence is not NodeSequence.NONE_SEQUENCE:
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
        if option is SequenceOption.NONE_OPTION:
            return True

        for sequence in option:
            if SequenceFinder.is_sequence_present_before(node, sequence, ignore_desc=option.ignore_desc):
                return True
        return False

    @staticmethod
    def is_sequence_present_before(node, sequence, ignore_desc=None):
        if sequence is not NodeSequence.NONE_SEQUENCE:
            ignore_desc = sequence.ignore_desc if ignore_desc is None else ignore_desc
            nodes_before = SequenceFinder._get_n_non_ignored_before(len(sequence), node, ignore_desc)
            for index, node_before in enumerate(nodes_before):
                if not sequence[index].is_match(node_before):
                    return False
        return True

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
    Requires n+1 whitespace sequences to be provided for n css nodes: before, inner and after nodes
    """
    def __init__(self, sequence_options, ignore_desc=None):
        self.sequence_options = sequence_options
        self.ignore_desc = ignore_desc

    def is_fulfilled(self, nodes):
        assert len(nodes) > 0
        first_child = nodes[0]
        return self._is_before_fulfilled(first_child) and \
            self._are_inner_and_after_fulfilled(nodes)

    def _are_inner_and_after_fulfilled(self, nodes):
        if len(self.sequence_options) < 2:
            return True
        inner_and_after_options = self.sequence_options[1:]
        for index, option in enumerate(inner_and_after_options):
            node = nodes[index]
            if not SequenceFinder.is_option_present_after(node, option):
                return False
        return True

    def _is_before_fulfilled(self, first_child_index):
        if len(self.sequence_options) < 2:
            return True
        before_option = self.sequence_options[0]
        return SequenceFinder.is_option_present_before(first_child_index, before_option)


class Convention(object):

    @abc.abstractmethod
    def is_violated(self, tree):
        pass


class IfThenConvention(Convention):

    def __init__(self, sequence, requirement):
        self._sequence = sequence
        self._requirement = requirement
        self._finder = SequenceFinder()

    def is_violated(self, tree):
        for nodes in self._finder.find_sequence(tree, self._sequence):
            print(self._requirement.is_fulfilled(nodes))
        # TODO: return useful information about the result


class ForbidConvention(Convention):

    def is_violated(self, tree):
        pass


class ConventionsMap(object):

    def __init__(self, conventions):
        self.conventions = conventions

    def __iter__(self):
        return self.conventions.__iter__()


class Walker(object):
    def find_pattern(self, tree, pattern):
        """
        Traverses a tree and returns all occurrences of a given pattern
        """
        if pattern.is_empty():
            return
        for start in self.find_node_in_tree(tree, pattern[0]):
            success, nodes = self.try_match_pattern(start, pattern)
            if success:
                yield nodes

    def try_match_pattern(self, node, pattern):
        """
        Returns 1. if the node and its siblings follow the given pattern
        2. the nodes that form the pattern
        """
        success, current = self._get_first_not_ignored(node, pattern.ignore_desc)
        current_desc = pattern[0]
        if not success or not current_desc.is_match(current):
            return False, None
        result = [current]
        for i in range(1, len(pattern)):
            sibling_desc = pattern[i]
            match, sibling = self.is_next_sibling(current, sibling_desc, pattern.ignore_desc)
            if not match:
                return False, None
            result.append(sibling)
            current = sibling
        return True, result

    def find_node_in_tree(self, node, desc):
        """
        Returns all nodes that match a given pattern
        """
        if desc.is_match(node):
            yield node
        if node.has_children():
            for child in node.value:
                yield from self.find_node_in_tree(child, desc)

    def is_next_sibling(self, start_node, sibling_desc, desc_ignores):
        """
        Returns 1. if the next sibling matches a specified descriptor and 2. the sibling
        """
        exists, sibling = self.get_next_sibling(start_node, desc_ignores)
        if exists and sibling_desc.is_match(sibling):
            return True, sibling
        return False, None

    def _get_first_not_ignored(self, node, ignore_desc):
        """
        If node is not ignored, returns node; Otherwise returns the next non-ignored sibling
        """
        if self._is_ignored(node, ignore_desc):
            return self.get_next_sibling(node, ignore_desc)
        return True, node

    def get_next_sibling(self, node, desc_ignores):
        """
        Returns 1. boolean if a sibling exists and 2. the next sibling
        Ignores the specified nodes
        """
        if node.has_parent():
            children = node.parent.value

            for index in range(node.index + 1, len(children)):
                sibling = children[index]
                if not self._is_ignored(sibling, desc_ignores):
                    return True, sibling
        return False, None

    def _is_ignored(self, node, ignore_desc):
        return ignore_desc.is_match(node)