"""
Your task is to write a function which returns the sum of following series up
to nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:
You need to round the answer to 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""


def series_sum(n):
    if n <= 1:
        return f"{n:.2f}"
    else:
        sum = 0.0
        for i in range(0, n):
            sum += 1 / (1 + (3 * i))
        return f"{sum:.2f}"


def refactored_series_sum(n):
    sum = 0.0
    for i in range(0, n):
        divisor = 1 + (3 * i)
        sum += 1 / divisor
    return f"{sum:.2f}"


# ---------------------------------- TESTS ----------------------------------
print("-------INITIAL TESTS-------")
test1 = series_sum(1)
solution1 = "1.00"
print(f"{test1} should = {solution1}")

test2 = series_sum(2)
solution2 = "1.25"
print(f"{test2} should = {solution2}")

test3 = series_sum(5)
solution3 = "1.57"
print(f"{test3} should = {solution3}")

test4 = series_sum(0)
solution4 = "0.00"
print(f"{test4} should = {solution4}")


print("-------REFACTORED TESTS-------")
test5 = refactored_series_sum(1)
test6 = refactored_series_sum(2)
test7 = refactored_series_sum(5)
test8 = refactored_series_sum(0)

print(
    f"{test5} should = 1.00 \n{test6} should = 1.25 \n{test7} should = 1.57 \n{test8} should = 0.00 "
)
