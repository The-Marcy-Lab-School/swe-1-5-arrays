import inspect
import random
import string

from modify import unpack_coordinates, uppercase_all

TEST_SUITE_NAME = "Modify Tests"


def test_uppercase_all():
    """uppercase_all - No matter how many words passed in, they are uppercased"""
    assert uppercase_all("hello", "world") == ["HELLO", "WORLD"]
    assert uppercase_all("hello", "my", "name", "is", "bob") == [
        "HELLO", "MY", "NAME", "IS", "BOB",
    ]
    assert uppercase_all("hello") == ["HELLO"]

    rand_str = "".join(random.choices(string.ascii_lowercase, k=10))
    assert uppercase_all(rand_str) == [rand_str.upper()]

    assert uppercase_all() == []


def test_unpack_coordinates():
    """unpack_coordinates - Unpacks the coordinates list into x and y variables"""
    source = inspect.getsource(unpack_coordinates)

    # The old way of pulling values out by index should be gone...
    assert "coordinates[0]" not in source
    assert "coordinates[1]" not in source
    # ...but the f-string must be left exactly as it is.
    assert 'f"X is: {x}, Y is: {y}"' in source

    assert unpack_coordinates([1, 2]) == "X is: 1, Y is: 2"
    assert unpack_coordinates([3, 4]) == "X is: 3, Y is: 4"
