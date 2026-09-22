from from_scratch import (
    add_to_front_or_back,
    delete_from_middle,
    get_all_y_coordinates,
    insert_into_middle,
    is_right_index,
    new_list_full_of,
    reverse_string,
    round_all_nums_down,
)

TEST_SUITE_NAME = "From Scratch Tests"


def test_add_to_front_or_back():
    """add_to_front_or_back - MUTATION - adds value to the front or back"""
    list1 = [1, 2, 3, 4, 5]
    add_to_front_or_back(list1, 6, False)
    assert list1 == [1, 2, 3, 4, 5, 6]

    list2 = [1, 2, 3, 4, 5]
    add_to_front_or_back(list2, 0, True)
    assert list2 == [0, 1, 2, 3, 4, 5]

    list3 = []
    add_to_front_or_back(list3, 1, False)
    assert list3 == [1]


def test_reverse_string():
    """reverse_string - PURE - returns a reversed string"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("hello world") == "dlrow olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def test_new_list_full_of():
    """new_list_full_of - PURE - returns a list full of the given value"""
    assert new_list_full_of(5, 3) == [5, 5, 5]
    assert new_list_full_of("a", 2) == ["a", "a"]
    assert new_list_full_of(None, 3) == [None, None, None]
    assert new_list_full_of(0, 0) == []


def test_insert_into_middle():
    """insert_into_middle - MUTATION - inserts value into the middle of a list"""
    list1 = [1, 2, 3, 4, 5]
    insert_into_middle(list1, 6)
    assert list1 == [1, 2, 6, 3, 4, 5]

    list2 = [1, 2, 3]
    insert_into_middle(list2, 0)
    assert list2 == [1, 0, 2, 3]

    list3 = ["a", "b", "c", "d"]
    insert_into_middle(list3, "z")
    assert list3 == ["a", "b", "z", "c", "d"]

    list4 = []
    insert_into_middle(list4, 1)
    assert list4 == [1]


def test_delete_from_middle():
    """delete_from_middle - MUTATION - deletes value from the middle of a list"""
    list1 = [1, 2, 3, 4, 5]
    delete_from_middle(list1)
    assert list1 == [1, 2, 4, 5]

    list2 = [1, 2, 3]
    delete_from_middle(list2)
    assert list2 == [1, 3]

    list3 = ["a", "b", "c", "d"]
    delete_from_middle(list3)
    assert list3 == ["a", "b", "d"]

    list4 = []
    delete_from_middle(list4)
    assert list4 == []


def test_is_right_index():
    """is_right_index - PURE - returns True if the index is the right index"""
    letters = ["a", "b", "c", "d", "e"]

    assert is_right_index(letters, "a", 0) is True
    assert is_right_index(letters, "a", 1) is False
    assert is_right_index(letters, "WOW", 1) is False
    assert is_right_index(letters, "A", 1) is False

    assert letters == ["a", "b", "c", "d", "e"]


def test_round_all_nums_down():
    """round_all_nums_down - PURE - rounds all numbers down"""
    list1 = [1.1, 2.2, 3.3]
    assert round_all_nums_down(list1) == [1, 2, 3]
    assert list1 == [1.1, 2.2, 3.3]

    # -7.9 rounds DOWN to -8, not -7
    list2 = [5.9, -7.9, 12.9]
    assert round_all_nums_down(list2) == [5, -8, 12]
    assert list2 == [5.9, -7.9, 12.9]

    list3 = [4.1, 12.2, 33.3]
    assert round_all_nums_down(list3) == [4, 12, 33]
    assert list3 == [4.1, 12.2, 33.3]

    list4 = [4, 5, 7]
    assert round_all_nums_down(list4) == [4, 5, 7]
    assert list4 == [4, 5, 7]


def test_get_all_y_coordinates():
    """get_all_y_coordinates - PURE - returns a list of all y coordinates"""
    list1 = [[1, 2], [3, 4], [5, 6]]
    assert get_all_y_coordinates(list1) == [2, 4, 6]
    assert list1 == [[1, 2], [3, 4], [5, 6]]

    # these are [x, y, z] coordinates
    list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert get_all_y_coordinates(list2) == [2, 5, 8]
    assert list2 == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    list3 = [[12.3, 81.3], [1.2, 3.4], [5.6, 7.8]]
    assert get_all_y_coordinates(list3) == [81.3, 3.4, 7.8]
    assert list3 == [[12.3, 81.3], [1.2, 3.4], [5.6, 7.8]]
