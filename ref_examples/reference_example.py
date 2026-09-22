"""
Play with this file. Nothing here is graded.

    python3 ref_examples/reference_example.py

In Python, a variable is a name pointing at an object. Assigning one name to
another points both names at the SAME object. It does not copy.
"""

# 1. Two names, one list. See two-names-one-list.png
nums = [1, 2, 3]
other = nums
other.append(4)
print(nums)          # [1, 2, 3, 4]  -- nums changed too
print(other is nums)  # True -- the same object, not a copy

# 2. A copy is a different object.
copied = nums[:]      # or list(nums), or nums.copy()
copied.append(5)
print(nums)           # [1, 2, 3, 4]  -- unchanged
print(copied is nums)  # False

# 3. Rebinding a name inside a function changes nothing outside it.
#    See rebinding-vs-mutating.png -- this is question 11.


def rebind(lst):
    lst = []          # points the local name at a new list


def mutate(lst):
    lst.clear()       # changes the list both names point at


letters = ["a", "b"]
rebind(letters)
print(letters)        # ['a', 'b'] -- untouched
mutate(letters)
print(letters)        # [] -- emptied

# 4. A shallow copy copies the outer list only.
inner1 = [1, 2]
inner2 = [3, 4]
outer = [inner1, inner2]
shallow = outer[:]
inner1.append("oh dear")
print(outer)          # [[1, 2, 'oh dear'], [3, 4]]
print(shallow)        # [[1, 2, 'oh dear'], [3, 4]]  -- same inner lists!

# Why does `shallow` show the change when it is a copy?
# That is the question to sit with.
