

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

    def is_undefined(self):
        return False

    def promote_to(self, type_):
        return self

    def promote_int_to(self, type_):
        return type_


class String(Type):
    def is_string(self):
        return True


class Decimal(Type):
    def is_numerical(self):
        return True

    def promote_int_to(self, type_):
        return self


class Integer(Type):
    def is_numerical(self):
        return True

    def promote_to(self, type_):
        return type_.promote_int_to(self)


class Boolean(Type):
    def is_boolean(self):
        return True


class CocoNodeType(Type):
    def is_css_node_type(self):
        return True


class CssNode(Type):
    def is_css_node(self):
        return True


class CocoNode(Type):
    def is_coco_node(self):
        return True


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
    def is_undefined(self):
        return True

String.TYPE = String()
Integer.TYPE = Integer()
Decimal.TYPE = Decimal()
Boolean.TYPE = Boolean()
CssNode.TYPE = CssNode()
CocoNodeType.TYPE = CocoNodeType()
CocoNode.TYPE = CocoNode()
Error.TYPE = Error()
