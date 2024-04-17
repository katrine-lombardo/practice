"""
1. Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
"""


def find_smallest_int(arr):
    return sorted(arr)[0]
    # return min(arr)


## TESTS

input1 = [34, 15, 88, 2]
solution1 = 2
print(find_smallest_int(input1))

input2 = [34, -345, -1, 100]
solution2 = -345
print(find_smallest_int(input2))
