"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

# STRATEGY
# Input: list of ints
# Output: int
# Notes: Edge cases to look out for can include empty lists, lists with equal
# frequency of occurring elements
# Logic:
# I can use a range and a pointer variable to map through the nums list and
# create a dictionary to hold the frequencies.
# I want to loop through the dictionary only once, perhaps comparing against a
# max value variable.
# Return the key corresponding to the value that has the highest frequency.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


solution = Solution()

nums = [3, 2, 3]
example1 = solution.majorityElement(nums)
print(f"{example1} should = 3")

nums = [2, 2, 1, 1, 1, 2, 2]
example2 = solution.majorityElement(nums)
print(f"{example2} should = 2")
