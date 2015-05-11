__author__ = 'boryana'


class NodeDescriptor(object):

    def __init__(self, type_=None, value=None):
        self.type_ = type_
        self.value = value
        self.search_by_type = self.type_ is not None
        self.search_by_value = self.value is not None

    def is_match(self, node):
        return self._match_type(node.type_) and self._match_value(node.value)

    def _match_value(self, node_value):
        if self.search_by_value:
            return self.value == node_value
        return True

    def _match_type(self, node_type):
        if self.search_by_type:
            return self.type_ == node_type
        return True

    def __str__(self):
        type_str = (' type=' + self.type_) if self.search_by_type else ''
        value_str = (' value=' + self.value) if self.search_by_value else ''
        return ''.join([' Descriptor:', type_str, value_str])

NodeDescriptor.ANY = NodeDescriptor()

WHITESPACE_PATTERN = [NodeDescriptor(type_='space'),
                      NodeDescriptor(type_='indent'),
                      NodeDescriptor(type_='tab'),
                      NodeDescriptor(type_='newline')]


class NodePattern(object):

    def __init__(self, descriptors, ignores):
        self.descriptors = descriptors
        self.ignores = ignores

    def __getitem__(self, i):
        return self.descriptors[i]

    def is_empty(self):
        return len(self.descriptors) == 0

    def __len__(self):
        return len(self.descriptors)


class Requirement(object):

    def __init__(self, before_pattern=None, inner_patterns=None, after_pattern=None, ignore_list=None):
        self.before_pattern = [] if before_pattern is None else before_pattern
        self.inner_patterns = [] if inner_patterns is None else inner_patterns
        self.after_pattern = [] if after_pattern is None else after_pattern
        self.ignore_list = [] if ignore_list is None else ignore_list

    def is_fulfilled(self, nodes):
        assert len(nodes) > 0
        parent = nodes[0].parent
        first_child = nodes[0]
        last_child = nodes[-1]
        return self._is_before_fulfilled(parent, first_child.index) and \
            self._is_after_fulfilled(parent, last_child.index) and \
            self._is_inner_fulfilled(parent, nodes)

    def _is_before_fulfilled(self, parent, first_child_index):
        if self._is_before_empty():
            return True
        start_index = first_child_index - len(self.before_pattern)
        if self._is_index_out_of_bounds(start_index, parent.value):
            return False

        pattern_start = parent.value[start_index]
        before_pattern = NodePattern(self.before_pattern, self.ignore_list)
        success, s = Walker().try_match_pattern(pattern_start, before_pattern)
        return success

    def _is_after_fulfilled(self, parent, last_child_index):
        if self._is_after_empty():
            return True
        if self._is_index_out_of_bounds(last_child_index, parent.value):
            return False

        pattern_index = parent.value[last_child_index + 1]
        after_pattern = NodePattern(self.after_pattern, self.ignore_list)
        success, s = Walker().try_match_pattern(pattern_index, after_pattern)
        return success

    def _is_inner_fulfilled(self, parent, nodes):
        if self._is_inner_empty():
            return True
        for index, desc in enumerate(self.inner_patterns):
            pattern = self._get_pattern(desc)
            first_sibling = parent.value[nodes[index].index + 1]
            success, _ = Walker().try_match_pattern(first_sibling, pattern)
            if not success:
                return False
        return True

    def _get_pattern(self, desc):
        res = desc if type(desc) is list else [desc]
        return NodePattern(res, self.ignore_list)

    def _is_before_empty(self):
        return len(self.before_pattern) == 0

    def _is_inner_empty(self):
        return len(self.inner_patterns) == 0

    def _is_after_empty(self):
        return len(self.after_pattern) == 0

    def _is_index_out_of_bounds(self, index, list):
        # The index should not point to the last element
        return index < 0 or index >= len(list) - 1


class Convention(object):

    def __init__(self, pattern, requirement):
        self.pattern = pattern
        self.requirement = requirement


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
        success, current = self._get_first_not_ignored(node, pattern.ignores)
        current_desc = pattern[0]
        if not success or not current_desc.is_match(current):
            return False, None
        result = [current]
        for i in range(1, len(pattern)):
            sibling_desc = pattern[i]
            match, sibling = self.is_next_sibling(current, sibling_desc, pattern.ignores)
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
        for desc in ignore_desc:
            if desc.is_match(node):
                return True
        return False