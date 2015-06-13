# This implementation is taken from http://tavianator.com/the-visitor-pattern-in-python/

# registry = {}
#
#
# class MultiMethod(object):
#     def __init__(self, name):
#         self.name = name
#         self.type_map = {}
#
#     def __call__(self, *args):
#         types = tuple(arg.__class__ for arg in args) # a generator expression!
#         function = self.type_map.get(types)
#         if function is None:
#             raise TypeError("no match")
#         return function(*args)
#
#     def register(self, types, function):
#         if types in self.type_map:
#             raise TypeError("duplicate registration")
#         self.type_map[types] = function
#
#
# def visitor(*types):
#     def register(function):
#         name = function.__name__
#         mm = registry.get(name)
#         if mm is None:
#             mm = registry[name] = MultiMethod(name)
#         mm.register(types, function)
#         return mm
#     return register

def _qualname(obj):
    """
    Get the fully-qualified name of an object (including module).
    """
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """
    Get the name of the class that declared an object.
    """
    name = _qualname(obj)
    return name[:name.rfind('.')]

# Stores the actual visitor methods
_methods = {}


def _visitor_impl(self, *arg):
    """
    Actual visitor method implementation.
    """
    method = _methods[(_qualname(type(self)), type(arg[0]))]
    return method(self, *arg)


def visitor(arg_type):
    """
    Decorator that creates a visitor method.
    """
    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator

