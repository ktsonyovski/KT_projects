import pytest
from new_exec import string_reverser, isstringpalidrome

def test_string_reverser_raise_value_error():
    with pytest.raises(ValueError):
        string_reverser(12)

def test_string_reverser_success():
    assert string_reverser("Hello") == "olleH"  # Check if "Hello" is reversed correctly

def test_isstringpalidrome_raise_value_error():
    with pytest.raises(ValueError):
        isstringpalidrome(132)
    
def test_isstringpalidrome_raise_value_error():
    assert isstringpalidrome("bob") == True