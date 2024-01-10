# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# Strategy:
# Create new_string variable to store output
# Loop through each letter in word
# Check if the letter equals its uppercase equivalent
# If it does not, append the letter to new_string
# If it does, join a space with the new letter and append this to new_string
# Return the new word
# Refactor the solution

def solution(s):
    new_string = ""
    for letter in s:
        if letter == letter.upper():
            new_letter = " " + letter
            new_string += new_letter
        else:
            new_string += letter
    return new_string


print(solution("camelCasing"))
print(solution("identifier"))
print(solution(""))
