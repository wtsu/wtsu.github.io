#https://leetcode.com/problems/merge-sorted-array/
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m+n -1 #the last element of the bigger index
        
        while m > 0 and n > 0: #continue this loop only as long as the  2 pointers are still trying to parse one of the words
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m += -1
            else: 
                nums1[last] = nums2[n-1]
                n += -1
            last += -1
        
        #fill nums1 with leftover elements in nums2
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n-1, last - 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s = Solution()
s.merge(nums1,m,nums2,n)
print(nums1)