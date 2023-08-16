#https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        #think of this in terms of a binary tree. where each node can split down two paths(1 step or 2 step)
        #when you build the binary tree, you will notice that is is really just performing the same calcs over again
        #you will then notice a pattern when you store the number of paths for the various sub problems
        one, two = 1,1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one

s = Solution()
print(s.climbStairs(5))