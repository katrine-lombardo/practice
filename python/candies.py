"""
n children have got m pieces of candy. They want to eat as much candy as they
can, but each child must eat exactly the same amount of candy as any other
child. Determine how many pieces of candy will be eaten by all the children
together. Individual pieces of candy cannot be split.

Example

For n = 3 and m = 10, the output should be
solution(n, m) = 9.

Each child will eat 3 pieces. So the answer is 9.
"""


def solution(n, m):
    return m - (m % n)


print("-------TESTS-------")
test1 = solution(3, 10)
test2 = solution(1, 2)
test3 = solution(10, 5)
if test1 == 9 and test2 == 2 and test3 == 0:
    print("Yay! All tests passed")
else:
    print("Errors")
