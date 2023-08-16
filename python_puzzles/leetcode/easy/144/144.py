from typing import Optional

#https://www.youtube.com/watch?v=afTpieEZXck&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=3
#https://leetcode.com/problems/binary-tree-preorder-traversal/

'''
redo #1 
- pay attention to when dealing with pointers to objects. You want attributes of the pointed at object, not just the entire object.
'''

lass TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        #psuedocode
        #1. create 3 variables
        #results -> the solution
        #stack -> use to log the next node to investigate
        #pointer -> to indicate what node to be looking at

        #2. Loop through each node. This can be accomplished by looping as long as the pointer or stack is "existent"
        
        #3. during each loop do the following: 
        #if the pointer is a real node, then add the pointer to results. add to the stack, the right child node. set pointer to the left child node.
        #if the pointer is a non existent node, then pop off the stack. set this popped off value as the next pointer

        #4. Once all nodes have been investigated, return results

        results = []
        stack = []
        pointer = root

        while pointer or stack: 
            if pointer: 
                results.append(pointer.val)
                stack.append(pointer.right)
                pointer = pointer.left
            else: 
                pointer = stack.pop()

        return results

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

s1 = Solution()
print(s1.preorderTraversal(root))