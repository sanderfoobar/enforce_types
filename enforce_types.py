#!/usr/bin/python3
import inspect
from inspect import isfunction, ismodule
import os
from functools import wraps

__author__ = "Sander Ferdinand"
__date__ = 2017

BASE = "%s/" % os.path.dirname(os.path.abspath(__file__))


def enforce_type(f):
    """
    Decorator for checking annotated type hints
    at runtime. Verifies input and output. Raises
    TypeError on conflict.
    """
    signature = inspect.signature(f)

    @wraps(f)
    def wrapped(*args, **kwargs):
        annotation_args = {k: v for k, v in f.__annotations__.items()
                           if not k == "return"}
        bound_args = signature.bind(*args, **kwargs).arguments
        for name, type_ in annotation_args.items():
            if not isinstance(bound_args[name], type_):
                raise TypeError('function %s argument \'%s\' must be of type \'%s\'' % (
                    f.__qualname__, str(name), str(type_.__qualname__)))
        rtn = f(*args, **kwargs)
        if "return" in f.__annotations__:
            if not isinstance(rtn, f.__annotations__["return"]):
                raise TypeError("function %s returned type \'%s\' while \'%s\' is required" % (
                    f.__qualname__, type(rtn).__qualname__,
                    f.__annotations__["return"].__qualname__))
        return rtn
    return wrapped


def enforce_all():
    """
    Finds all type hints annotated
    functions declared within the
    scope of this project and
    monkey patches them with the
    `enforce_type` decorator
    :return:
    """
    frame = _top_frame()
    module = inspect.getmodule(frame.frame)
    patch_module(module)


def patch_module(m):
    members = inspect.getmembers(m, predicate=_validate)
    for member in members:
        if isfunction(member[1]):
            patch_function(m, member[1])
        elif ismodule(member[1]):
            patch_module(member[1])


def patch_function(m, f):
    setattr(m, f.__qualname__, enforce_type(f))
    print("[patched->%s->%s()]" % (m.__name__, f.__name__))


def _validate(obj):
    if not isfunction(obj) and not ismodule(obj) or not obj:
        return
    try:
        filepath = inspect.getfile(obj)
    except TypeError:
        return
    if filepath == __file__ or not filepath.startswith(BASE):
        return
    if inspect.isfunction(obj) and not obj.__annotations__:
        return
    return obj


def _top_frame():
    for frame in inspect.stack()[::-1]:
        if frame[1].startswith(BASE) and not inspect.getfile(frame.frame) == __file__:
            return frame
    raise Exception("top frame could not be found")
