"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
solution(n) = 99.
"""


def solution(n):
    result = ""
    for num in range(0, n):
        result += "9"
    return int(result)


print("-------TESTS-------")
test1 = solution(2)
test2 = solution(1)
test3 = solution(7)
if test1 == 99 and test2 == 9 and test3 == 9999999:
    print("Yay! All tests passed")
else:
    print("Errors")
