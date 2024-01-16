"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m +
n, where the first m elements denote the elements that should be merged, and
the last n elements are set to 0 and should be ignored. nums2 has a length of
n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
"""

# STRATEGY
# Input: 2 lists, 2 ints
# Output: Nothing --> Modify nums1 in place
# 1. Modify nums2 so that it contains the correct number of items, n
# 2. Modify nums1 so that it contains the correct number of items, m
# 3. Merge both lists
# 4. Sort the list


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])


def leetcode_merge(nums1, m, nums2, n):
    nums1[:] = sorted(nums1[0:m] + nums2[0:n])
    return nums1


leetcode_merge_1 = leetcode_merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(f"{leetcode_merge_1} should be [1, 2, 2, 3, 5, 6]")

leetcode_merge_2 = leetcode_merge([1], 1, [], 0)
print(f"{leetcode_merge_2} should be [1]")

leetcode_merge_3 = leetcode_merge([0], 0, [1], 1)
print(f"{leetcode_merge_3} should be [1]")
