"""
The provided code stub will read in a dictionary containing key/value pairs of
name: [marks] for a list of students. Print the average of the marks array for
the student name provided, showing 2 places after the decimal.

Sample 1 Input:
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika
Sample 2 Output: 56.00

Sample 1 Input:
    2
    Harsh 25 26.5 28
    Anurag 26 28 30
    Harsh
Sample 1 Output: 26.50
"""

# NOTES
# Input: Multiple lines - int, then x numbers of strings (including ints) then a
# string corresponding to a particular name.
# Output: Float
# Strategy: Figure out how to isolate the items on each line to handle the logic
# on the individual pieces. The first line int tells me how many rows of data to
# expect, so that should help me to isolate that data.
# Based on the input type, it seems like a good structure for the lines of data
# would be a dict, with k = name and v = list of grades.
# Once the dict is populated I can lookup a particular name in the dict, and
# manually calculate the average of the items in the list.
## Chatted to GrandPa Ted and walked through the code below to better understand
## how the input was split - Every day's a school day :)

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    names_scores = student_marks[query_name]
    avg = sum(names_scores) / len(names_scores)
    print(f"{avg:.2f}")

# -----------------------------------------------------------------------------
# Experimental testing zone


def process_sample(sample):
    n = int(sample[0])
    student_marks = {}
    for line in sample[1:-1]:
        name, *scores = line.split()
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = sample[-1]

    names_scores = student_marks[query_name]
    avg = sum(names_scores) / len(names_scores)
    print(f"{avg:.2f}")
    return f"{avg:.2f}"


sample0 = ["3", "Krishna 67 68 69", "Arjun 70 98 63", "Malika 52 56 60", "Malika"]
sample1 = ["2", "Harsh 25 26.5 28", "Anurag 26 28 30", "Harsh"]

result0 = process_sample(sample0)
print(f"{result0} should = 56.00")

result1 = process_sample(sample1)
print(f"{result1} should = 26.50")
