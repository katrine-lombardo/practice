"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.
"""


def solution(n, firstNumber):
    halfway = int(n / 2) + firstNumber
    if halfway > n:
        return halfway - n
    elif halfway == n:
        return 0
    else:
        return halfway


def refactored_solution(n, firstNumber):
    return (firstNumber + (n / 2)) % n


print("-------TESTS-------")
test1 = solution(10, 2)
solution1 = 7
test2 = solution(18, 6)
solution2 = 15
test3 = solution(6, 3)
solution3 = 0
if test1 == solution1 and test2 == solution2 and test3 == solution3:
    print("Yay! All tests passed")
else:
    print("Errors")


test4 = refactored_solution(10, 2)
test5 = refactored_solution(18, 6)
test6 = refactored_solution(6, 3)
if test4 == solution1 and test5 == solution2 and test6 == solution3:
    print("Yay! All tests passed")
else:
    print("Errors")
