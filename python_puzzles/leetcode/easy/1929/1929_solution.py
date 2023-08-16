from typing import List

#https://leetcode.com/problems/concatenation-of-array/
#https://www.youtube.com/watch?v=68isPRHgcFQ&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=4

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums: 
                ans.append(n)
        return ans
    
s = Solution()

print(s.getConcatenation([1,2,3,4]))