'''
redo #1: 
- be careful with booleans, use False and True and not F/T/false/true
'''

from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack = [root]
        visit = [False]
        result = []

        while stack: 
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v == True: 
                    result.append(cur.val)
                else: 
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)
        return result
    
# Example Tree
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(3)
#     5
#    / \
#   1   4
#      / \
#     2   3

s1 = Solution()
print(s1.postorderTraversal(root))