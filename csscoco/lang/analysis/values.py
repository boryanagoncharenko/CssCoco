

class Value(object):

    def is_false(self):
        raise ValueError()

    def not_(self):
        raise ValueError()

    def unary_minus(self):
        raise ValueError()

    def and_(self, value):
        raise ValueError()

    def and_bool(self, value):
        raise ValueError()

    def or_(self, value):
        raise ValueError()

    def or_bool(self, value):
        raise ValueError()

    def equals(self, value):
        raise ValueError()

    def equals_integer(self, value):
        raise ValueError()

    def equals_decimal(self, value):
        raise ValueError()

    def equals_boolean(self, value):
        raise ValueError()

    def equals_string(self, value):
        raise ValueError()

    def not_equals(self, value):
        raise ValueError()

    def not_equals_integer(self, value):
        raise ValueError()

    def not_equals_decimal(self, value):
        raise ValueError()

    def not_equals_boolean(self, value):
        raise ValueError()

    def not_equals_string(self, value):
        raise ValueError()

    def greater_than(self, value):
        raise ValueError()

    def greater_than_integer(self, value):
        raise ValueError()

    def greater_than_decimal(self, value):
        raise ValueError()

    def greater_than_equals(self, value):
        raise ValueError()

    def greater_than_equals_integer(self, value):
        raise ValueError()

    def greater_than_equals_decimal(self, value):
        raise ValueError()

    def less_than(self, value):
        raise ValueError()

    def less_than_integer(self, value):
        raise ValueError()

    def less_than_decimal(self, value):
        raise ValueError()

    def less_than_equals(self, value):
        raise ValueError()

    def less_than_equals_integer(self, value):
        raise ValueError()

    def less_than_equals_decimal(self, value):
        raise ValueError()

    def is_(self, value):
        raise ValueError()

    def is_of_type(self, value):
        raise ValueError()

    def in_(self, value):
        raise ValueError()

    def in_list(self, value):
        raise ValueError()


class Decimal(Value):
    def __init__(self, value):
        super(Decimal, self).__init__()
        self.value = value

    def equals(self, value):
        return value.equals_decimal(self)

    def equals_integer(self, value):
        return Boolean.build(value.value == self.value)

    def equals_decimal(self, value):
        return Boolean.build(value.value == self.value)

    def not_equals(self, value):
        return value.not_equals_decimal(self)

    def not_equals_integer(self, value):
        return Boolean.build(value.value != self.value)

    def not_equals_decimal(self, value):
        return Boolean.build(value.value != self.value)

    def greater_than(self, value):
        return value.greater_than_decimal(self)

    def greater_than_integer(self, value):
        return Boolean.build(value.value > self.value)

    def greater_than_decimal(self, value):
        return Boolean.build(value.value > self.value)

    def greater_than_equals(self, value):
        return value.greater_than_equals_decimal(self)

    def greater_than_equals_integer(self, value):
        return Boolean.build(value.value >= self.value)

    def greater_than_equals_decimal(self, value):
        return Boolean.build(value.value >= self.value)

    def less_than(self, value):
        return value.less_than_decimal(self)

    def less_than_integer(self, value):
        return Boolean.build(value.value < self.value)

    def less_than_decimal(self, value):
        return Boolean.build(value.value < self.value)

    def less_than_equals(self, value):
        return value.less_than_equals_decimal(self)

    def less_than_equals_integer(self, value):
        return Boolean.build(value.value <= self.value)

    def less_than_equals_decimal(self, value):
        return Boolean.build(value.value <= self.value)


class Integer(Value):
    def __init__(self, value):
        super(Integer, self).__init__()
        self.value = value

    def unary_minus(self):
        return Integer(-self.value)

    def equals(self, value):
        return value.equals_integer(self)

    def equals_integer(self, value):
        return Boolean.build(value.value == self.value)

    def equals_decimal(self, value):
        return Boolean.build(value.value == self.value)

    def not_equals(self, value):
        return value.not_equals_integer(self)

    def not_equals_integer(self, value):
        return Boolean.build(value.value != self.value)

    def not_equals_decimal(self, value):
        return Boolean.build(value.value != self.value)

    def greater_than(self, value):
        return value.greater_than_integer(self)

    def greater_than_integer(self, value):
        return Boolean.build(value.value > self.value)

    def greater_than_decimal(self, value):
        return Boolean.build(value.value > self.value)

    def greater_than_equals(self, value):
        return value.greater_than_equals_integer(self)

    def greater_than_equals_integer(self, value):
        return Boolean.build(value.value >= self.value)

    def greater_than_equals_decimal(self, value):
        return Boolean.build(value.value >= self.value)

    def less_than(self, value):
        return value.less_than_integer(self)

    def less_than_integer(self, value):
        return Boolean.build(value.value < self.value)

    def less_than_decimal(self, value):
        return Boolean.build(value.value < self.value)

    def less_than_equals(self, value):
        return value.less_than_equals_integer(self)

    def less_than_equals_integer(self, value):
        return Boolean.build(value.value <= self.value)

    def less_than_equals_decimal(self, value):
        return Boolean.build(value.value <= self.value)

    def in_(self, value):
        return value.in_list(self)


class String(Value):
    def __init__(self, value):
        super(String, self).__init__()
        self.value = value

    def equals(self, value):
        return value.equals_string(self)

    def equals_string(self, value):
        return Boolean.build(value.value == self.value)

    def not_equals(self, value):
        return value.not_equals_string(self)

    def not_equals_string(self, value):
        return Boolean.build(value.value != self.value)

    def in_(self, value):
        return value.in_list(self)

String.EMPTY = String('')


class Boolean(Value):
    def __init__(self, value):
        super(Boolean, self).__init__()
        self.value = value

    @staticmethod
    def build(bool_value):
        return Boolean.TRUE if bool_value else Boolean.FALSE

    def is_false(self):
        return not self.value

    def not_(self):
        return Boolean.build(not self.value)

    def and_(self, value):
        return value.and_bool(self)

    def and_bool(self, value):
        return Boolean.build(value.value and self.value)

    def or_(self, value):
        return value.or_bool(self)

    def or_bool(self, value):
        return Boolean.build(value.value or self.value)

    def equals(self, value):
        return value.equals_boolean(self)

    def equals_boolean(self, value):
        return Boolean.build(value.value == self.value)

    def not_equals(self, value):
        return value.not_equals_boolean(self)

    def not_equals_boolean(self, value):
        return Boolean.build(value.value != self.value)

    def in_(self, value):
        return value.in_list(self)

Boolean.FALSE = Boolean(False)
Boolean.TRUE = Boolean(True)


class NodeType(Value):
    def __init__(self, value):
        super(NodeType, self).__init__()
        self.value = value

    def is_of_type(self, node_value):
        real_node = node_value.value
        return Boolean.build(real_node.matches(self.value))


class Node(Value):
    def __init__(self, node):
        assert node
        self.value = node

    def is_(self, value):
        return value.is_of_type(self)


class List(Value):
    def __init__(self, value):
        super(List, self).__init__()
        self.value = value

    def in_list(self, operand):
        for v in self.value:
            if operand.equals(v).value:
                return Boolean.TRUE
        return Boolean.FALSE


class Undefined(Value):
    pass

Undefined.VALUE = Undefined()
