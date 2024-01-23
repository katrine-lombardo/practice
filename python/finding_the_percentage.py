"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

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
if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
