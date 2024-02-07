"""
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that
checks whether the two arrays have the "same" elements, with the same
multiplicities (the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared,
regardless of the order.
"""

# NOTES
# Input: two lists
# Output: bool
# These instructions are complex so let's break it down: The expected output is
# "True" if the elements in each array are the "same".
# "Same", in this case, means that each element of listb equals any element of
# lista squared.
# Edge cases: Empty arrays, arrays of nonstandard characters, null arrays,
# arrays not equal in length
# Logic:
# Rather than check if each element is a square root, I'll multiply each element
# of listA by itself.
# From there, I now can exit the function early if at any point we encounter an
# element of listB that does not exist in listA.
# To compare the lists I will initially loop through listB, before refactoring
# for time complexity.


def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    if len(array1) != len(array2):
        return False

    array1_squared = [elem * elem for elem in array1]

    array1_squared.sort()
    array2.sort()
    return True if array1_squared == array2 else False


# example1 = comp(
#     [121, 144, 19, 161, 19, 144, 19, 11],
#     [121, 14641, 20736, 361, 25921, 361, 20736, 361],
# )
# print(f"{example1} should = True")

# example2 = comp(
#     [121, 144, 19, 161, 19, 144, 19, 11],
#     [132, 14641, 20736, 361, 25921, 361, 20736, 361],
# )
# print(f"{example2} should = False")

example3 = comp(
    [2, 2, 3],
    [4, 9, 9],
)
print(f"{example3} should = False")
