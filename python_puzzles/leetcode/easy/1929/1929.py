from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums: 
                ans.append(n)
        return ans    
s = Solution()

print(s.getConcatenation([1,2,3,4]))