"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

# STRATEGY
# Input: List of ints
# Output: List of ints
# Logic: I can map out the list, using a dictionary to track the frequency
# of each element in the list.
# A simpler solution would be to use set, which removes duplicates in place.
# This might be considered a bit cheaty but it works.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return list(set(nums))


solution = Solution()

nums = [1, 1, 2]
result1 = solution.removeDuplicates(nums)
print(f"ex. 1:  {result1} should = [1, 2]")

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = solution.removeDuplicates(nums)
print(f"ex. 2:  {result2} should = [0, 1, 2, 3, 4]")
