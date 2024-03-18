"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example

For a = [50, 60, 60, 45, 70], the output should be
solution(a) = [180, 105].
"""

# Input: list
# Output: list of two ints
# Goal: Return the sum of the two teams. People are divided into teams: Team 1 contains all odd idx, and team 2 contains even idx.
# Approach: (edge cases: empty lists)
# 1. Set some constant variable to house the running weight total for each team.
# 2. Enumerate through list to extract the correct weights based on whether the index is divisible by 2 or not or is zero.
# 3. Refactor to minimise the number of lines / space.
# 4. Refactor for time complexity.
# Note: I wouldn't want to refactor further because I want to maintain human readability.


def solution(a):
    team1 = 0
    team2 = 0

    for index, weight in enumerate(a):
        if index == 0:
            team1 += weight
        elif index % 2 == 0:
            team1 += weight
        else:
            team2 += weight

    return [team1, team2]


def refactored_solution(a):
    team1 = sum(weight for idx, weight in enumerate(a) if idx % 2 == 0 or idx == 0)
    team2 = sum(weight for idx, weight in enumerate(a) if idx % 2 != 0)
    return [team1, team2]


# ------- TESTS -------
print("-------TESTS-------")
test1 = solution([50, 60, 60, 45, 70])
test2 = solution([100, 50])
test3 = solution([80])

print(
    f"{test1} should = [180, 105]\n{test2} should = [100, 50]\n{test3} should = [80, 0]"
)

test4 = refactored_solution([50, 60, 60, 45, 70])
test5 = refactored_solution([100, 50])
test6 = refactored_solution([80])

print(
    f"{test4} should = [180, 105]\n{test5} should = [100, 50]\n{test6} should = [80, 0]"
)
