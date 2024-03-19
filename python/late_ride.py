"""
One night you go for a ride on your motorcycle. At 00:00 you start your engine,
and the built-in timer automatically begins counting the length of your ride, in
minutes. Off you go to explore the neighborhood.

When you finally decide to head back, you realize there's a chance the bridges
on your route home are up, leaving you stranded! Unfortunately, you don't have
your watch on you and don't know what time it is. All you know thanks to the
bike's timer is that n minutes have passed since 00:00.

Using the bike's timer, calculate the current time. Return an answer as the sum
of digits that the digital timer in the format hh:mm would show.

Example

For n = 240, the output should be
solution(n) = 4.

Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0
+ 4 + 0 + 0 = 4, which is the answer.

For n = 808, the output should be
solution(n) = 14.

808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 =
14.
"""


def solution(n):
    hh = int(n / 60)
    mm = n - (hh * 60)
    string = "".join(str(hh) + str(mm))
    total = 0
    for num in string:
        total += int(num)
    return total


def refactored_solution(n):
    hh = int(n / 60)
    mm = n % 60
    return (hh % 10) + int(hh / 10) + (mm % 10) + int(mm / 10)


print("-------TESTS-------")
test1 = solution(240)
solution1 = 4
test2 = solution(808)
solution2 = 14
test3 = solution(1439)
solution3 = 19
print(
    "Yay, all tests passed"
    if test1 == solution1 and test2 == solution2 and test3 == solution3
    else "Errors"
)

test4 = refactored_solution(240)
test5 = refactored_solution(808)
test6 = refactored_solution(1439)
print(
    "Yay, all tests passed refactored solution"
    if test4 == solution1 and test5 == solution2 and test6 == solution3
    else "Errors in refactored solution"
)
