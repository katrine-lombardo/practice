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
    if n == 0:
        return f"{n:.2f}"
    else:
        solution = ""

        return solution


# ---------------------------------- TESTS ----------------------------------

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
