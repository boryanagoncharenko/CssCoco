__author__ = 'boryana'


class Value(object):
    pass


class Integer(Value):
    def __init__(self, value):
        self.value = value


class String(Value):
    def __init__(self, value):
        self.value = value


class Boolean(Value):
    def __init__(self, value):
        self.value = value

# TODO: try to build this in the class
@staticmethod
def build_bool(value):
    return Boolean.TRUE if value else Boolean.FALSE

Boolean.FALSE = Boolean(False)
Boolean.TRUE = Boolean(True)


class NodeType(Value):
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
        self.search_by_type = self.type_
        self.search_by_value = self.value

    def is_node_of_type(self, node_value):
        node = node_value.value
        return self._is_type_match(node) and self._is_value_match(node)

    def _is_type_match(self, node):
        if self.search_by_type:
            return self.type_ == node.type_
        return True

    def _is_value_match(self, node):
        if self.search_by_value:
            return self.value == node.value
        return True


class Node(Value):
    # TODO: this value should not be here
    def __init__(self, node):
        self.value = node


class List(Value):
    def __init__(self, value):
        self.value = value
