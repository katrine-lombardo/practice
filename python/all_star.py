"""
Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.
"""

# NOTES
# Input: two strings
# Output: int
# Goal: Find the number of times a character is found in a string
# Edge cases: Empty strings, non-letter characters
# Plan: Use a counter variable set to zero, iterate through the string and
# increment the counter if the letter is equal to the character. This can be
# done with a for loop, or refactored with list comprehension.


def str_count(strng, letter):
    # counter = 0
    # for char in strng:
    #     if letter == char:
    #         counter += 1
    # return counter
    return len([char for char in strng if char == letter])


example1 = str_count("Hello", "o")
print(example1)

example2 = str_count("Hello", "l")
print(example2)

example3 = str_count("", "z")
print(example3)
