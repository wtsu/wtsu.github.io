#https://leetcode.com/problems/sqrtx/
#https://www.youtube.com/watch?v=zdMhGxRWutQ&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW

class Solution():
    def mySqrt(self, x: int) -> int:
        #psuedocode
        #go "through" all the factors possible between 0 and x
        #use a binary search so that you don't literally go through each factor. 
        #example of binary search on 8
            #1. search space at first is 0, 8

            #2. first midpoint is 3
                #0 + (8-1)//2
                #0 + 7//2
                #7/2 = 3.5, so 7//2 = 3

            #3. midpoint of 3 is too high. search space is below 3
                #3*3 = 9 > x
                #0, 2

            #4. midpoint of 2 is too low. It could be the anser. Search space is above 3
                #2 * 2 = 4 < x
                #answer is suspected to be 2

            #5. it isnt possible for the search space to be above 3, since that was already rejected in a prior iteration. This confirms the answer is 2
                #3,2 
                #answer is therefore 2
        
        res = 0
        #initialize variables for binary search
        l, r = 0, x

        while l <= r: #this is the break condition to get out of doing the search
            #find the first midpoint
            m = l + ((r-1)//2)
            
            if m * m > x:
                #limit search space to the second half 
                r = m - 1
                #this condition can never return the sqrt
            elif m * m < x:
                #limit search space to the first half
                l = m + 1
                #you may have also found the sqrt
                res = m
            else:
                return m
        return res

s1 = Solution()

print(s1.mySqrt(4))