from typing import Optional
#https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #base case where root does not exist
            return None
        
        #perform the inversion on the root
        temp = root.left
        root.left = root.right
        root.right = root.left 

        #use recursion and perform this on the child nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        

        return root

a1 = TreeNode(1)
a3 = TreeNode(3)
a2 = TreeNode(2,a1,a3)

s = Solution()

s.invertTree(a2)
