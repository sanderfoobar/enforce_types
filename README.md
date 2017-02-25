# Enforce_types.py

*__Enforce.py__* is a Python 3.5+ library for type validation through annotated functions. It uses the standard type hinting syntax (defined in PEP 484).

**NOTICE:** Python versions 3.5.2 and earlier (3.5.0-3.5.2) are now deprecated. Only Python versions 3.5.3+ are be supported.

### Features

#### Basic type hint enforcement

```python
>>> from enforce_types import enforce_type
>>>
>>> @enforce_type
... def foo(bar: str) -> None:
...     print(bar)
>>>
>>> foo('Hello World')
Hello World
>>>
>>> foo(5)
Traceback (most recent call last):
  File "/home/dsc/PycharmProjects/enforce_types/main.py", line 15, in <module>
    foo.simple_type_hinted_function(2)
  File "/home/dsc/PycharmProjects/enforce_types/enforce_types.py", line 29, in wrapped
    f.__qualname__, str(name), str(type_.__qualname__)))
TypeError: function foo argument 'bar' must be of type 'str'
>>>
```

#### Monkey patch all annotated functions

```python
>>> import foo

>>> # type not enforced yet
>>> foo.simple_type_hinted_function(2)

>>> from enforce_types import enforce_all
>>> enforce_all()

>>> # type enforced now, exception
>>> foo.simple_type_hinted_function(2)

Traceback (most recent call last):
  File "/home/dsc/PycharmProjects/enforce_types/main.py", line 15, in <module>
    foo.simple_type_hinted_function(2)
  File "/home/dsc/PycharmProjects/enforce_types/enforce_types.py", line 29, in wrapped
    f.__qualname__, str(name), str(type_.__qualname__)))
TypeError: function simple_type_hinted_function argument 'bar' must be of type 'str'
```
