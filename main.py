import foo

def unused_test_function(foo):
    return foo

# type not enforced yet
print("[call] simple_type_hinted_function()")
foo.simple_type_hinted_function(2)

from enforce_types import enforce_all
enforce_all()

# type enforced now, exception
print("[call] simple_type_hinted_function()")
foo.simple_type_hinted_function(2)
