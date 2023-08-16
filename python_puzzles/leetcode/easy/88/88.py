#https://leetcode.com/problems/merge-sorted-array/
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_ptr = (m + n) - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_ptr] = nums1[m-1]
                m += -1
            else:
                nums1[last_ptr] = nums2[n-1]
                n += -1
            last_ptr += -1

        while n > 0:
            nums1[last_ptr] = nums2[n-1]
            n += -1
            last_ptr += -1

nums1 = [2,2,3,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3

s = Solution()
s.merge(nums1,m,nums2,n)
print(nums1)