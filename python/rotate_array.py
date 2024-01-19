"""
Given an integer array nums, rotate the array to the right by k steps, where k
is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""

# STRATEGY
# Input: list of ints, int
# Output: original list of ints modified
# Logic:
# I'm thinking that slicing might be the simplest method
# I would reassign the nums list to the sum of the two halves of the
# original list nums.
# If that doesn't work, perhaps I might enumerate to transverse through the list
# and get the right order.
# Notes: Edge cases might include k being greater than the length of the
# original list


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first_half = nums[-k:]
        second_half = nums[:-k]
        nums[:] = first_half + second_half
        return nums


solution = Solution()

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
example1 = solution.rotate(nums, k)
print(f"{example1} should = [5, 6, 7, 1, 2, 3, 4]")

nums = [-1, -100, 3, 99]
k = 2
example2 = solution.rotate(nums, k)
print(f"{example2} should = [3, 99, -1,-100]")
