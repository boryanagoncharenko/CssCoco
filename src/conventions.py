import src.sequences as seqs
from src.sequences import TreeWalker as walker


class Requirement(object):
    """
    Describes how the whitespaces around the css nodes should be
    Requires n+1 whitespace variations to be provided for n css nodes: before, inner and after nodes
    """
    def __init__(self, variation_list, ignore_desc=None):
        # assert len(variation_list) > 1
        self.variation_list = variation_list
        self.ignore_desc = ignore_desc

    def _is_present_error(self, present):
        return not present

    def is_fulfilled(self, nodes, variation_ignore_desc):
        assert len(nodes) > 0
        errs = []

        before_present = self.is_before_variation_present(nodes, variation_ignore_desc, errs)
        inner_present = self.are_inner_variations_present(nodes, errs)
        after_present = self.is_after_variation_present(nodes, variation_ignore_desc, errs)

        return (before_present and inner_present and after_present), errs

    def is_before_variation_present(self, nodes, variation_ignore_desc, errs):
        if self.variation_list[0] is seqs.SiblingsVariation.NONE:
            return True

        before_nodes = walker.get_non_ignored_nodes_before_node(nodes[0], variation_ignore_desc, self.ignore_desc)
        present, sequence, inner_nodes = walker.is_variation_exact_match(self.variation_list[0], before_nodes)
        is_error = self._is_present_error(present)
        if is_error:
            errs.append(self._get_err(nodes[0], self.variation_list[0], inner_nodes))
        return not is_error

    def are_inner_variations_present(self, nodes, errs):
        is_present = True
        for i in range(1, len(nodes)):
            variation = self.variation_list[i]
            if variation is not seqs.SiblingsVariation.NONE:
                start_node = nodes[i-1]
                end_node = nodes[i]
                present, sequence, inner_nodes = walker.is_variation_present_btw_two_nodes(variation, start_node,
                                                                                           end_node, self.ignore_desc)
                if self._is_present_error(present):
                    is_present = False
                    errs.append(self._get_err(start_node, variation, inner_nodes))
        return is_present

    def is_after_variation_present(self, nodes, variation_ignore_desc, errs):
        if self.variation_list[-1] is seqs.SiblingsVariation.NONE:
            return True
        after_nodes = walker.get_non_ignored_nodes_after_node(nodes[-1], variation_ignore_desc, self.ignore_desc)
        present, sequence, inner_nodes = walker.is_variation_exact_match(self.variation_list[-1], after_nodes)
        is_error = self._is_present_error(present)
        if is_error:
            errs.append(self._get_err(nodes[-1], self.variation_list[-1], inner_nodes))
        return not is_error

    def _get_err(self, start_node, variation, inner_nodes):
        return ''.join(['Violation on line ', str(start_node.start_position.line), ': expected ',
                        variation.to_error_string(), ', found ', self.error_msg(inner_nodes),' instead.'])

    def _get_nodes_before(self, start_node, variation_ignore_desc):
        before_node = self._get_before_node(start_node, variation_ignore_desc)
        if not before_node:
            return []
        nodes = start_node.parent.value[before_node.index+1:start_node.index]
        return self._sieve_the_non_ignored(nodes)

    def _get_before_node(self, start_node, variation_ignore_desc):
        parent = start_node.parent
        if not parent or start_node == 0:
            return None
        for i in range(start_node.index-1, 0, -1):
            prev_sibling = parent.value[i]
            if not variation_ignore_desc.is_match(prev_sibling):
                return prev_sibling
        return None

    def _get_nodes_after(self, start_node, variation_ignore_desc):
        after_node = self._get_after_node(start_node, variation_ignore_desc)
        if not after_node:
            return []
        nodes = start_node.parent.value[start_node.index+1:after_node.index]
        return self._sieve_the_non_ignored(nodes)

    def _get_after_node(self, start_node, variation_ignore_desc):
        parent = start_node.parent
        if not parent or start_node.index == len(parent.value) - 1:
            return None
        for i in range(start_node.index + 1, len(parent.value)):
            next_sibling = parent.value[i]
            if not variation_ignore_desc.is_match(next_sibling):
                return next_sibling
        return None

    def _is_inner_two(self, variation, node_start, node_end):
        assert node_start.parent is node_end.parent
        assert node_start.index < node_end.index
        assert variation is not seqs.SiblingsVariation.NONE

        parent = node_start.parent
        nodes = parent.value[node_start.index+1:node_end.index]
        nodes = self._sieve_the_non_ignored(nodes)
        return self._is_variation_match(variation, nodes)

    def _is_variation_match(self, variation, nodes):
        for sequence in variation:
            is_match = self._is_sequence_match(sequence, nodes)
            if is_match:
                return True, sequence, nodes
        return False, seqs.SiblingSequence.NONE, nodes

    def _is_sequence_match(self, sequence, nodes):
        if len(sequence) != len(nodes):
            return False  # There is a mismatch in the length
        for i, desc in enumerate(sequence):
            if not desc.is_match(nodes[i]):
                return False  # There is no match
        return True

    def _sieve_the_non_ignored(self, nodes):
        result = []
        for n in nodes:
            if not self.ignore_desc.is_match(n):
                result.append(n)
        return result

    def error_msg(self, nodes):
        res = ''
        for n in nodes:
            res = ''.join([res, n.to_error_string()])
        return ''.join(['\'', res, '\''])


class ForbidRequirement(Requirement):

    def __init__(self, variation_list, ignore_desc=None):
        Requirement.__init__(self, variation_list, ignore_desc)

    def is_fulfilled(self, nodes, variation_ignore_desc):
        errs = [self._get_err(nodes[0], None, nodes)]
        return False, errs

    def _is_present_error(self, present):
        return present

    def _get_err(self, start_node, variation, inner_nodes):
        return ''.join(['Violation on line ', str(start_node.start_position.line),
                        ': found forbidden sequence ', self.error_msg(inner_nodes)])


class NewCondition(object):
    """
    This class should know about the pattern it needs to seek (is it a sibling sequence or a child sequence)
    and about the specific filters applied to the pattern (where declaration is vendor-specific etc.)
    It should also know about the special ignores of the condition, e.g. when we say rule + rule (ignore whitespace)
    """
    pass
    # For 'rule rule' example this should return [rule_node, rule_node]
    # For 'rule >> id > word' this should return [rule, id, word]


class NewRequirement(object):
    """
    This class determines whether the convention is violated or not
    It either endures that there are sibling nodes ordered in the proper order
    or that the condition evaluates to True
    """
    pass
    # Contains a variation list to check the whitespacing
    # Contains an expressing that should evaluate to boolean


class NewConvention(object):

    def __init__(self, condition):
        self.condition = condition


class Convention(object):

    def __init__(self, cond_variation, requirement):
        self._cond_variation = cond_variation
        self._requirement = requirement

    def is_relaxed_by_convention(self, convention):
        return self._cond_variation.is_part_of_variation(convention._cond_variation)

    def is_strong(self):
        pass


class RequireConvention(Convention):

    def __init__(self, cond_variation, requirement):
        Convention.__init__(self, cond_variation, requirement)

    def is_strong(self):
        return True


class ForbidConvention(Convention):

    def _err(self, nodes):
        ns = ''
        for n in nodes:
            ns = ''.join([ns, n.to_error_string()])
        return ''.join(['\nViolation on line, ', str(nodes[0].start_position.line), ': forbidden sequence of \'', ns, '\''])

    def is_strong(self):
        return True


class AllowConvention(Convention):
    def is_strong(self):
        return False


class ConventionsMap(object):

    def __init__(self, conventions):
        strong, weak = self._separate_conventions(conventions)
        self.strong = strong
        self.weak = weak
        self._references = self._build_references(strong, weak)
        self._weak_matches = {}

    def _separate_conventions(self, conventions):
        strong = []
        weak = []
        for c in conventions:
            if c.is_strong():
                strong.append(c)
            else:
                weak.append(c)
        return strong, weak

    def _build_references(self, strong, weak):
        res = {}
        for s in strong:
            for w in weak:
                if s.is_relaxed_by_convention(w):
                    self._add_to_map(s, w, res)
        return res

    def _add_to_map(self, key, value, dictionary):
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]

    def find_violations(self, css_tree):
        self._weak_matches = self.mark_weak_matches(css_tree)
        res = []
        for s in self.strong:
            for nodes in walker.find_variation_in_tree(css_tree, s._cond_variation):
                is_fulfilled, errs = s._requirement.evaluate(nodes)
                if not is_fulfilled and not self._is_already_relaxed(s, nodes):
                    res = res + errs
        return res

    def mark_weak_matches(self, css_tree):
        res = {}
        for w in self.weak:
            for nodes in walker.find_variation_in_tree(css_tree, w._cond_variation):
                is_fulfilled, _ = w._requirement.evaluate(nodes)
                if is_fulfilled:
                    self._add_to_map(w, nodes, res)
        return res

    def _is_already_relaxed(self, s, nodes):
        if s not in self._references:
            return False
        for allow in self._references[s]:
            if allow in self._weak_matches:
                nodes_list = self._weak_matches[allow]
                if self._is_nodes_in_nodes_list(nodes, nodes_list):
                    return True
        return False

    def _is_nodes_in_nodes_list(self, nodes, nodes_list):
        for ns in nodes_list:
            if self._is_list_part_of_list(nodes, ns):
                return True
        return False

    def _is_list_part_of_list(self, list1, list2):
        assert list1
        assert list2
        if len(list2) < len(list1):
            return False

        for i in range(0, len(list2)):
            for j in range(0, len(list1)):
                if list1[j] != list2[i+j]:
                    break
                if j == len(list1) - 1:
                    return True
        return False
