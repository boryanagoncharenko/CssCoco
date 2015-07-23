# This implementation is taken from http://tavianator.com/the-visitor-pattern-in-python/
#
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
# def multimethod(*types):
#     def register(function):
#         name = function.__name__
#         mm = registry.get(name)
#         if mm is None:
#             mm = registry[name] = MultiMethod(name)
#         mm.register(types, function)
#         return mm
#     return register
#
#






def _qualname(obj):
    """
    Get the fully-qualified name of an object (including module).
    """
    r = obj.__module__ + '.' + obj.__qualname__
    return r

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
    q_name = _qualname(type(self))
    cur_name = type(arg[0])
    if (q_name, cur_name) in _methods:
        method = _methods[(q_name, cur_name)]
        return method(self, *arg)

    for base_name in _get_base_classes_names(arg[0].__class__):
        if (q_name, base_name) in _methods:
            method = _methods[(q_name, base_name)]
            return method(self, *arg)

    error = ''.join(['You must add a method that visits type ', arg[0].__class__.__name__, ' in class ', q_name])
    raise NotImplementedError(error)


def _get_base_classes_names(class_):
    result = []
    base = _get_base_class_name(class_)
    while base:
        result.append(base)
        base = _get_base_class_name(base)
    return result


def _get_base_class_name(class_):
    bases = class_.__bases__
    if bases:
        return bases[0]
    return None


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

