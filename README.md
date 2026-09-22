# Lists

Practise Python lists, and learn when a function changes a list instead of
returning a new one.

**Practising:** lists, mutation, pure functions

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are allowed.

**Tutor mode** — AI explains, questions, and critiques. You write every line
you submit. For this assignment: ask it why changing a list inside a function
can affect the caller. Do not ask it for the function.

**Implementer mode** — you write a spec first, AI writes code from it, you
verify. For this assignment: your spec must say, for each function, whether it
changes the list in place or returns a new one.

You own every line either way, and you will be asked to explain it.

## Setup

Work in `development/mod-1`. Make a draft branch before you start.

```sh
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
git checkout -b draft

pytest                     # run the tests
pytest -k reverse_string   # run one test
```

75% of tests passing counts as complete. Submit before it is perfect.

A **pure** function returns a new value and changes nothing else. A **side
effect** changes something outside the function, such as a list you passed in.
Only mutate when a question asks for it.

## From Scratch

Write your solutions in `src/from_scratch.py`.

### Question 1: `add_to_front_or_back` — MUTATES

Insert `value` into `lst`, at the front if `is_front` is `True`, otherwise at
the back. Change the list in place and return nothing.

```python
nums = [1, 2, 3]
add_to_front_or_back(nums, 0, True)
print(nums)   # [0, 1, 2, 3]
```

### Question 2: `reverse_string` — PURE

Return `text` reversed. Strings are immutable, so the original cannot change.

```python
reverse_string("hello")   # "olleh"
```

A slice can do this in one step.

### Question 3: `new_list_full_of` — PURE

Return a new list holding `value`, repeated `count` times.

```python
new_list_full_of(5, 3)     # [5, 5, 5]
new_list_full_of(0, 0)     # []
```

### Question 4: `insert_into_middle` — MUTATES

Insert `value` at the middle index of `lst`. Change the list in place and
return nothing. An empty list is still a valid input.

```python
nums = [1, 2, 3, 4, 5]
insert_into_middle(nums, 6)
print(nums)   # [1, 2, 6, 3, 4, 5]
```

Read the tests to see which index counts as the middle.

### Question 5: `delete_from_middle` — MUTATES

Remove whatever sits at the middle index of `lst`. Change the list in place
and return nothing. An empty list must not raise an error.

```python
nums = [1, 2, 3, 4, 5]
delete_from_middle(nums)
print(nums)   # [1, 2, 4, 5]
```

### Question 6: `is_right_index` — PURE

Return `True` if `value` sits at `index` in `lst`, and `False` otherwise.
A value that is not in the list returns `False`.

```python
letters = ["a", "b", "c"]
is_right_index(letters, "a", 0)     # True
is_right_index(letters, "WOW", 1)   # False
```

### Question 7: `round_all_nums_down` — PURE

Return a new list with every number in `nums` rounded down. Leave `nums`
alone.

```python
round_all_nums_down([5.9, -7.9, 12.9])   # [5, -8, 12]
```

Note `-7.9` rounds down to `-8`. Check what `int()` does to negatives first.

### Question 8: `get_all_y_coordinates` — PURE

Each item in `coords` is a coordinate list such as `[x, y]`. Return a new list
of only the `y` values, which are the second item in each one.

```python
get_all_y_coordinates([[1, 2], [3, 4], [5, 6]])      # [2, 4, 6]
get_all_y_coordinates([[1, 2, 3], [4, 5, 6]])        # [2, 5]
```

## Modify

Change the two functions already in `src/modify.py`.

### Question 9: `uppercase_all`

This only handles exactly three words. Make it take any number of words,
including none. Look up `*args`.

```python
uppercase_all("hello", "world")   # ["HELLO", "WORLD"]
uppercase_all()                   # []
```

We never pass a list, only separate word arguments.

### Question 10: `unpack_coordinates`

This pulls `x` and `y` out by index. Rewrite it to unpack both in one
statement, keeping the names `x` and `y`. The tests read the source and check
the f-string is untouched.

```python
unpack_coordinates([1, 2])   # "X is: 1, Y is: 2"
```

## Debug

Both functions in `src/debug.py` are broken.

### Question 11: `clear_list`

Should empty the given list in place. It does nothing. Work out what `lst = []`
rebinds, then fix it.

### Question 12: `get_first_item`

Should return the first item and leave the list untouched. It removes the item
instead. An empty list returns `None`.

## Bonus: names, objects, and copies

### Question 13: why does the copy change?

Run `python3 ref_examples/reference_example.py` and read it beside the two
diagrams there. Its last example copies a list, changes the original, and the
copy changes too. Why?

Nothing to submit.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Open a pull request to your instructor for feedback.
