from typing import Optional

#https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#https://www.youtube.com/watch?v=QhszUQhGGlA&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=2

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        #initialize Stack with root
        stack = [root]

        #initialize visit with False
        visit = [False]
        res = []

        cntr = 0

        while stack: #loop continues while curr or stack is populated
            #print functions to help see the logic
            print('\n')
            print(f'loop {cntr}')
            pretty_stack = []
            for i in stack: 
                try:
                    pretty_stack.append(i.val)
                except: 
                    pretty_stack.append('N')
            print(pretty_stack)
            print(f'visit: {visit}')
            print(f'res: {res}')

            #pop off the LIFO element
            #since stack and visit are meant to be aligned
            cur, v =  stack.pop(), visit.pop()
            if cur: 
                #if the node has been visited, then you add it to res
                if v: 
                    res.append(cur.val)
                
                #if the node has not been visited
                #append the cur node to the stack
                #append true since the node has been visited
                #append the two children nodes, in rigth then left order
                #append false twice since these children nodes would not have been visited
                else: 
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)
            #if curr is null, the LIFO would get popped off in the next run
            cntr += 1
        print('\n')
        print(f'loop {cntr}')
        pretty_stack = []
        for i in stack: 
            try:
                pretty_stack.append(i.val)
            except: 
                pretty_stack.append('N')
        print(pretty_stack)
        print(f'visit: {visit}')
        print(f'res: {res}')
        return res 

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
