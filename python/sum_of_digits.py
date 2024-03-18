"""
You are given a two-digit integer n. Return the sum of its digits.

For n = 29, the output should be solution(n) = 11.
"""

# Input: int
# Output: int
# Goal: Take each individual number of an integer, and return the sum of those.
# Approach: I can convert the initial number to a string, which will allow me to for loop over each "character" digit in the original int.
# 1. Start with traditional for loop to return correct solution.
# 2. Refactor to minimise the number of lines / space.
# 3. Refactor for time complexity.


def solution(n):
    stringed_n = str(n)

    result = 0
    for char in stringed_n:
        result += int(char)

    return result


def refactored_solution(n):
    return sum(int(char) for char in str(n))


# Time complexity is already optimal at O(1), since the loop doesn't depend on the input.

# ------- TESTS -------
print("------- TESTS -------")
test1 = solution(29)
print(f"{test1} should = 11 \n ")


test2 = refactored_solution(29)
print(f"{test2} should = 11 \n ")
