"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
"""


def solution(a, b):
    if a == b:
        return True

    swaps = 0
    swap_locations = []

    for i in range(len(a)):
        if a[i] != b[i]:
            swaps += 1
            swap_locations.append(i)
            if swaps > 2:
                return False

    if swaps == 0:
        return True

    if swaps == 2:
        swap_1_a = a[swap_locations[0]]
        swap_2_a = a[swap_locations[1]]
        swap_1_b = b[swap_locations[0]]
        swap_2_b = b[swap_locations[1]]

        if swap_1_a == swap_2_b and swap_2_a == swap_1_b:
            return True
        else:
            return False

    return False


# -------TESTS-------

a1 = [1, 2, 3]
b1 = [1, 2, 3]
test1 = solution(a1, b1)
solution1 = True

a2 = [1, 2, 3]
b2 = [2, 1, 3]
test2 = solution(a2, b2)
solution2 = True

a3 = [1, 2, 2]
b3 = [2, 1, 1]
test3 = solution(a3, b3)
solution3 = False

if test1 == solution1 and test2 == solution2 and test3 == solution3:
    print("Yay! All tests passed")
else:
    print("Errors")
