from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #res defined as a list (res = [0]) is mutable and allows for modification inside the inner function. 
        #However, res as an integer (res = 0) is immutable.
        res = [0]
        def get_height(root):
            if not root: 
                return -1
            
            left = get_height(root.left)
            right = get_height(root.right)
            diameter = 2 + left + right 
            res[0] = max(res[0],diameter)
            height = 1 + max(left,right)
            return height

        get_height(root)

        return res[0]


#     1
#    / \ 
#   2   3
#  / \   
# 4   5   

a4 = TreeNode(4)
a5 = TreeNode(5)
a3 = TreeNode(3)
a2 = TreeNode(2,a4,a5)
a1 = TreeNode(1,a2,a3)

s = Solution()
print(s.diameterOfBinaryTree(a1))