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

    def __eq__(self, other):
        return (type(other) is type(self)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

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

    def to_error_string(self):
        return str(self.value)


class NegativeSimpleDescriptor(SimpleDescriptor):

    def __init__(self, type_=None, value=None):
        super(NegativeSimpleDescriptor, self).__init__(type_, value)
        # SimpleDescriptor.__init__(type_=type_, value=value)

    def is_match(self, node):
        is_match = super(NegativeSimpleDescriptor, self).is_match(node)
        return not is_match


class CompoundDescriptor(NodeDescriptor):
    """
    Contains a list of SimpleDescriptors and tries to match with any of them
    """
    def __init__(self, descriptors):
        self.descriptors = descriptors

    def __eq__(self, other):
        return (type(other) is type(self)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

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

    def to_error_string(self):
        return 'Compound'

NodeDescriptor.ANY = SimpleDescriptor()

NodeDescriptor.WHITESPACE = CompoundDescriptor([SimpleDescriptor(type_='space'),
                                                SimpleDescriptor(type_='indent'),
                                                SimpleDescriptor(type_='tab'),
                                                SimpleDescriptor(type_='newline')])

NodeDescriptor.INDENT = CompoundDescriptor([SimpleDescriptor(type_='indent')])

NodeDescriptor.COMMENT = CompoundDescriptor([SimpleDescriptor(type_='comment')])