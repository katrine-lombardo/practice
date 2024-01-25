"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set
A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set
B.

Sample Input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output:
True
False
False
"""

# NOTES
# Input: Integers separated by line
# Output: bool separated by line
# It's not super clear what makes up the input, so let's think it through:
# - If line one = idx 0, we can separate the test cases by dividing the sum of
#     the lines after idx 0 by the value of line at idx 0.
# - So testcase1 always begins on line 1, testcase2 will begin on line 5,
#   testcase3 will begin on line 9, etc...
# - This means that a test case takes up 4 lines every time.
# Strategy:
# I'll want to separate the input into separate variables, to make it easier to
# work with.
# I'll need to iterate through each test case, likely needing an empty variable
# to store the results.
# I'll be able to check if the items in A are a subset of B by converting the
# input line into a set, and using the built-in method "issubset" to print
# either true or false.


input = """
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
"""

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        num_elems_A = int(input())
        A = set(map(int, input().split()))
        num_elems_B = int(input())
        B = set(map(int, input().split()))

        print(A.issubset(B))
