#https://leetcode.com/problems/two-sum/description/
#https://www.youtube.com/watch?v=9UtInBqnCgA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[num] = i 
        return 
    
nums = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums, target))