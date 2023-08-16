#https://leetcode.com/problems/symmetric-tree/description/
#https://www.youtube.com/watch?v=Mao9uzxwvmc&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=5

from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #psuedologic: 
        #solve using recursion and a DFS algorithm
        #create a dfs function
            #base case will be:
                # if two nodes being compared are both null then return true
                # if one of the two nodes are null then return False
            #otherwise, compare the value of the left and right node

        def dfs(left, right):
            #base case
            if not left and not right:
                return True
            
            #check if one is null and the other is not
            if not left or not right:
                return False
            
            return (left.val == right.val 
             and dfs(left.left, right.right) 
             and dfs(left.right, right.left))
        return dfs(root.left,root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

s = Solution()

print(s.isSymmetric(root))
