"""
In this kata, you will write a function that receives an array of string and
returns a string that is either 'naughty' or 'nice'. Strings that start with
the letters b, f, or k are naughty. Strings that start with the letters g, s, or
n are nice. Other strings are neither naughty nor nice.

If there is an equal amount of bad and good actions, return 'naughty'

Examples:

bad_actions = [
    'broke someone\'s window',
    'fought over a toaster',
    'killed a bug'
]
whatListAmIOn(bad_actions)
#-> 'naughty'

good_actions = [
    'got someone a new car',
    'saved a man from drowning',
    'never got into a fight'
]
what_list_am_i_on(good_actions)
#-> 'nice'

actions = [
    'broke a vending machine',
    'never got into a fight',
    'tied someone\'s shoes'
]
what_list_am_i_on(actions)
#-> 'naughty'
"""

# NOTES
# Input: List
# Output: String
# Thoughts/edge cases: Actions on neither list, empty list of actions, equal
# amount of actions good and bad
# Logic:
# 1. Transverse through input list
# 2. Create variable to store count for each actions
# 3. Compare count of actions and return highest


def what_list_am_i_on(actions):
    bad_action_letters = ["b", "f", "k"]
    good_action_letters = ["g", "s", "n"]
    bad_actions_count = 0
    good_actions_count = 0

    for action in actions:
        if action[0] in bad_action_letters:
            bad_actions_count += 1
        elif action[0] in good_action_letters:
            good_actions_count += 1

    return "nice" if good_actions_count > bad_actions_count else "naughty"


# ---------------------------------- TESTS ----------------------------------

actions1 = ["broke someone's window", "fought over a toaster", "killed a bug"]
example1 = what_list_am_i_on(actions1)
print(f"{example1} should = naughty")

actions2 = [
    "got someone a new car",
    "saved a man from drowning",
    "never got into a fight",
]
example2 = what_list_am_i_on(actions2)
print(f"{example2} should = nice")

actions3 = [
    "broke a vending machine",
    "never got into a fight",
    "tied someone's shoes",
]
example3 = what_list_am_i_on(actions3)
print(f"{example3} should = naughty")
