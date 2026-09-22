from debug import clear_list, get_first_item

TEST_SUITE_NAME = "Debug Tests"


def test_clear_list():
    """clear_list - removes all elements from a list as a mutation"""
    list1 = [1, 2, 3, 4, 5]
    clear_list(list1)
    assert list1 == []

    list2 = ["a", "b", "c"]
    clear_list(list2)
    assert list2 == []

    list3 = []
    clear_list(list3)
    assert list3 == []


def test_get_first_item():
    """get_first_item - returns the first item in a list WITHOUT mutating original"""
    list1 = [1, 2, 3, 4, 5]
    assert get_first_item(list1) == 1
    assert list1 == [1, 2, 3, 4, 5]

    list2 = ["a", "b", "c"]
    assert get_first_item(list2) == "a"
    assert list2 == ["a", "b", "c"]

    list3 = []
    assert get_first_item(list3) is None
    assert list3 == []
