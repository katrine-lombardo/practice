"""
Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.

Example

For divisor = 3 and bound = 10, the output should be
solution(divisor, bound) = 9.

The largest integer divisible by 3 and not larger than 10 is 9.
"""


def solution(divisor, bound):
    return bound - (bound % divisor)


print("-------TESTS-------")
test1 = solution(3, 10)
solution1 = 9
test2 = solution(2, 7)
solution2 = 6
test3 = solution(10, 50)
solution3 = 50
if test1 == solution1 and test2 == solution2 and test3 == solution3:
    print("Yay! All tests passed")
else:
    print("Errors")
