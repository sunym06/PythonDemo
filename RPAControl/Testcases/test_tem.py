import pytest


@pytest.mark.parametrize("a, b", [("A", "B"), ("A1", "B1")])
def test_add(a,b):
    print("a+b:", a, b)
