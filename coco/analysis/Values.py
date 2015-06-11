

class Value(object):

    def is_false(self):
        raise ValueError()

    def and_(self, value):
        raise ValueError()

    def and_bool(self, value):
        raise ValueError()

    def equals(self, value):
        raise ValueError()

    def equals_integer(self, value):
        raise ValueError()

    def equals_boolean(self, value):
        raise ValueError()

    def equals_string(self, value):
        raise ValueError()

    def is_(self, value):
        raise ValueError()

    def is_of_type(self, value):
        raise ValueError()


class Integer(Value):
    def __init__(self, value):
        self.value = value

    def equals(self, value):
        return value.equals_integer(self)

    def equals_integer(self, value):
        return Boolean.build(value.value == self.value)


class String(Value):
    def __init__(self, value):
        self.value = value

    def equals(self, value):
        return value.equals_string(self)

    def equals_string(self, value):
        return Boolean.build(value.value == self.value)


class Boolean(Value):
    def __init__(self, value):
        self.value = value

    @staticmethod
    def build(bool_value):
        return Boolean.TRUE if bool_value else Boolean.FALSE

    def is_false(self):
        return not self.value

    def and_(self, value):
        return value.and_bool(self)

    def and_bool(self, value):
        return Boolean.build(value.value and self.value)

    def equals(self, value):
        return value.equals_boolean(self)

    def equals_boolean(self, value):
        return Boolean.build(value.value == self.value)

Boolean.FALSE = Boolean(False)
Boolean.TRUE = Boolean(True)


class NodeType(Value):
    def __init__(self, type_=None, value=None):
        self.type_ = type_
        self.value = value

    def is_of_type(self, node_value):
        real_node = node_value.value

        return self._is_type_match(real_node) and self._is_value_match(real_node)

    def _is_type_match(self, node):
        if not node:
            pass
        if self.type_:
            return self.type_ == node.type_
        return True

    def _is_value_match(self, node):
        if self.value:
            return self.value == node.value
        return True


class Node(Value):
    # TODO: this value should not be here
    def __init__(self, node):
        assert node
        self.value = node

    def is_(self, value):
        return value.is_of_type(self)


class List(Value):
    def __init__(self, value):
        self.value = value


class Undefined(Value):
    def __init__(self):
        pass

Undefined.VALUE = Undefined()