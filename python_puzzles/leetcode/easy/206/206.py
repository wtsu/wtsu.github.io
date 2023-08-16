from typing import Optional
#https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursion method:
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        # return newHead

        prev, cur = None, head

        while cur: 
            next = cur.next
            cur.next = prev
            prev = cur 
            cur = next
        
        return prev

a3 = ListNode(3,None)
a2 = ListNode(2,a3)
a1 = ListNode(1,a2)

s = Solution()
x = s.reverseList(a1) 
print(x.val)