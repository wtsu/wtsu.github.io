
'''
redo #1: 
-be careful with the while condition
-be careful with elif vs if
'''

class Solution():
    def mySqrt(self, x: int) -> int:
        #initialize variables
        left,right = 0, x
        res = 0 

        while left <= right: 
            midpoint = left + ((right - left) // 2)
            if midpoint*midpoint > x: 
                right = midpoint - 1
            elif midpoint*midpoint < x:
                left = midpoint + 1
                res = midpoint
            else:
                return midpoint
        return res

s1 = Solution()

print(s1.mySqrt(4))
