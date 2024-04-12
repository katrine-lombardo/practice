"""
Some phone usage rate may be described as follows:

- first minute of a call costs min1 cents,
- each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
- each minute after 10th costs min11 cents.

You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?

Example:
For min1 = 3, min2_10 = 1, min11 = 2, and s = 20, the output should be
solution(min1, min2_10, min11, s) = 14.
"""

# Input: int (x4)
# Output: int
# Objective: Find the greatest number of minutes possible from x cents.
# Notes: I'm given the rate for each type of minute, so won't need to calculate
# that. min2_10 rates apply for 9 minutes total, and minute11 for all beyond.
# Strategy:
# 1. Check if I have zero cents, or not enough for one minute.
# 2. Start a balance variable to track remaining cents, and minute tracker.
# 3. For minute 1: If the balance is equal to or greater than min1, subtract
#    min1 from the balance and add one to the minute tracker.
# 4. For minutes 2 - 10: If the balance is >= min2_10 * 9, I can add 9 minutes
#    to the minute tracker and decrement the balance by min2_10 * 9.
# 5. For all minutes after 11: Get the number of remaining minutes achievable by
#    floor dividing the balance by the min11 rate and adding this to the
#    tracker.


def solution(min1, min2_10, min11, s):
    balance = s - min1
    if balance < 0:
        return 0

    # First minute
    minute_tracker = 1

    # Minutes 2 - 10
    for minute in range(2, 11):
        if balance >= min2_10:
            minute_tracker += 1
            balance -= min2_10
        else:
            break

    # Minutes 11+
    if balance > 0 and minute_tracker >= 10:
        remaining_minutes = balance // min11
        minute_tracker += remaining_minutes

    return minute_tracker


def refactored_solution(min1, min2_10, min11, s):
    if s < min1:
        return 0
    elif s >= min1 and s <= min1 + 9 * min2_10:
        return 1 + (s - min1) // min2_10
    return 10 + (s - min1 - 9 * min2_10) // min11


# ---------- TESTING ----------

solution1 = 14
test1 = solution(3, 1, 2, 20)
print(f"Test1 = {test1 == solution1}")

solution2 = 1
test2 = solution(2, 2, 1, 2)
print(f"Test2 = {test2 == solution2}")

solution3 = 11
test3 = solution(10, 1, 2, 22)
print(f"Test3 = {test3 == solution3}")

solution4 = 3
test4 = solution(1, 2, 1, 6)
print(f"Test4 = {test4 == solution4}")

reftest1 = refactored_solution(3, 1, 2, 20)
print(f"Refest1 = {reftest1 == solution1}")

reftest2 = refactored_solution(2, 2, 1, 2)
print(f"Refest2 = {reftest2 == solution2}")

reftest3 = refactored_solution(10, 1, 2, 22)
print(f"Refest3 = {reftest3 == solution3}")

reftest4 = refactored_solution(1, 2, 1, 6)
print(f"Refest4 = {reftest4 == solution4}")
