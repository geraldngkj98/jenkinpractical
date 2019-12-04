import pytest
from Hello_World import *

#wassup

def test_hello():
    result = hello()
    assert result == "Hello!"
