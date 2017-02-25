import urllib
from urllib.parse import quote_plus

simple_constant = quote_plus("<foo>")


def simple_type_hinted_function(bar: str) -> str:
    return bar
