from typing import Optional
#https://leetcode.com/problems/palindrome-linked-list/

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #array soln
        # res = []

        # while head: 
        #     res.append(head.val)
        #     head = head.next

        # left, right = 0, len(res)-1

        # while right >= left:
        #     if res[right] != res[left]: 
        #         return False 
        #     else:
        #         left += 1
        #         right -= 1
        # return True


        #find midpoint then reverse linked list 
        fast, slow = head, head
        
        #finds the midpoint via slow
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        
        #reverses the second half of the linked list
        prev = None
        while slow: 
            temp = slow.next
            slow.next = prev #reverses the linked list(note it doesn't "do" this the first time the loop happens)
            prev = slow 
            slow = temp #increments slow up
        
        left, right = head, prev 

        while right: 
            if left.val != right.val:
                return False
            else:
                left = left.next 
                right = right.next 
        return True


a4 = ListNode(1,)
a3 = ListNode(2,a4)
a2 = ListNode(2,a3)
a1 = ListNode(1,a2)

s = Solution()
print(s.isPalindrome(a1))