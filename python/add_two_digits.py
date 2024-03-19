"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
solution(n) = 11.
"""


def solution(n):
    first_digit = int(str(n)[0:1])
    second_digit = int(str(n)[1:])
    return first_digit + second_digit


print("-------TESTS-------")
test1 = solution(29)
test2 = solution(48)
test3 = solution(10)
if test1 == 11 and test2 == 12 and test3 == 1:
    print("Yay! All tests passed")
else:
    print("Errors")
