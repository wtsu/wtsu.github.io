from typing import Optional

#https://www.youtube.com/watch?v=afTpieEZXck&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=3
#https://leetcode.com/problems/binary-tree-preorder-traversal/

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        cur, stack = root, []
        res = []
        cntr = 0

        while cur or stack: 
            print('\n')
            print(f'loop : {cntr}')
            if cur:
                print(f'cur : {cur.val}')
            else:
                print(f'cur : ''N')

            pretty_stack = []
            for s in stack: 
                if s:
                    pretty_stack.append(s.val)
                else: 
                    pretty_stack.append('N')
            print(f'stack : {pretty_stack}')
            print(f'res : {res}')
            
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
            cntr += 1
        
        print('\n')
        if cur:
            print(f'cur : {cur.val}')
        else:
            print(f'cur : ''N')
        print(f'loop : {cntr}')
        pretty_stack = []
        for s in stack: 
            if s:
                pretty_stack.append(s.val)
            else: 
                pretty_stack.append('N')
        print(f'stack : {pretty_stack}')
        print(f'res : {res}')
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

s1 = Solution()
s1.preorderTraversal(root)