'''
redo #1 
- pay attention to the colon after else
'''

from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left == None  and right == None:
                return True
            
            if left == None or right == None:
                return False

            is_symmetric = (left.val == right.val and
                            dfs(left.left, right.right) and 
                            dfs(left.right, right.left)
                            )
            return is_symmetric
        
        return(dfs(root.left, root.right))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

s = Solution()

print(s.isSymmetric(root))

