"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

# STRATEGY
# Input: List of ints
# Output: List of ints
# Logic: My original instinct was to use a set, but it does not preserve order,
# so I'll need to ensure the converted list is sorted.
# My second solution is a more manual solution which better preserves time
# complexity, in comparison to my original solution (O(n2) --> O(n))
# Using a range to map through nums, I only need to loop over the list one time.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return nums

    def removeDuplicates2(self, nums):
        if not nums:
            return 0

        last = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[last]:
                last += 1
                nums[last] = nums[i]

        return nums[: last + 1]


solution = Solution()

nums = [1, 1, 2]
result1 = solution.removeDuplicates(nums)
print(f"ex. 1:  {result1} should = [1, 2]")

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = solution.removeDuplicates(nums)
print(f"ex. 2:  {result2} should = [0, 1, 2, 3, 4]")

nums = [-1, 0, 0, 0, 0, 3, 3]
result3 = solution.removeDuplicates(nums)
print(f"ex. 3:  {result3} should = [-1, 0, 3]")

nums = [1, 1, 2]
result4 = solution.removeDuplicates2(nums)
print(f"ex. 4:  {result4} should = [1, 2]")

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result5 = solution.removeDuplicates2(nums)
print(f"ex. 5:  {result5} should = [0, 1, 2, 3, 4]")

nums = [-1, 0, 0, 0, 0, 3, 3]
result6 = solution.removeDuplicates(nums)
print(f"ex. 6:  {result6} should = [-1, 0, 3]")
