# Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The order of the elements may be changed. Then return the
# number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to
# get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the
# elements which are not equal to val. The remaining elements of nums are not
# important as well as the size of nums.
# Return k.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]


# STRATEGY
# Input: list of ints, int
# Output: int
# 1. Remove val anywhere it appears within the list (don't make a copy)
# 2. Return the length of the updated list


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [num for num in nums if num != val]
        return len(nums)


# TESTING

solution = Solution()

nums1 = [3, 2, 2, 3]
val1 = 3
result1 = solution.removeElement(nums1, val1)
print(f"[EXAMPLE 1] {result1} = 2? {nums1} = [2, 2]?")

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
result2 = solution.removeElement(nums2, val2)
print(f"[EXAMPLE 2] {result2} = 5? {nums2} = [0, 1, 4, 0, 3]?")
