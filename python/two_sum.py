"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""

# NOTES
# Input: List and int
# Output: List
# Logic: Find the two list items that when added together equal the target. I
# can find all permutations by looping through the list using enumerate. After
# that, I can find the index associated with both values by looking up the
# results in the dictionary.
# Edge cases: Empty lists, target equal to zero


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results_dict = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in results_dict:
                return [results_dict[difference], index]
            results_dict[num] = index
        return []


solution = Solution()

nums = [2, 7, 11, 15]
target = 9
example1 = solution.twoSum(nums, target)
print(f"{example1} should = [0,1]")

nums = [3, 2, 4]
target = 6
example2 = solution.twoSum(nums, target)
print(f"{example2} should = [1,2]")

nums = [3, 3]
target = 6
example3 = solution.twoSum(nums, target)
print(f"{example3} should = [0,1]")
