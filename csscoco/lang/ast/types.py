

class Type(object):
    def is_numerical(self):
        return False

    def is_string(self):
        return False

    def is_boolean(self):
        return False

    def is_list(self):
        return False

    def is_css_node(self):
        return False

    def is_css_node_type(self):
        return False

    def is_coco_node(self):
        return False

    def is_error(self):
        return False

    def promote_to(self, type_):
        return self

    def promote_int_to(self, type_):
        return type_


class String(Type):
    def is_string(self):
        return True

String.TYPE = String()


class Decimal(Type):
    def is_numerical(self):
        return True

    def promote_int_to(self, type_):
        return self

Decimal.TYPE = Decimal()


class Integer(Type):
    def is_numerical(self):
        return True

    def promote_to(self, type_):
        return type_.promote_int_to(self)

Integer.TYPE = Integer()


class Boolean(Type):
    def is_boolean(self):
        return True

Boolean.TYPE = Boolean()


class CssNodeType(Type):
    def is_css_node_type(self):
        return True

CssNodeType.TYPE = CssNodeType()


class CssNode(Type):
    def is_css_node(self):
        return True

CssNode.TYPE = CssNode()


class CocoNode(Type):
    def is_coco_node(self):
        return True

CocoNode.TYPE = CocoNode()


class List(Type):
    def __init__(self, elements_type):
        super(List, self).__init__()
        self.elements_type = elements_type

    def is_list(self):
        return True

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False


class Error(Type):
    def is_error(self):
        return True

Error.TYPE = Error()
