from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1: 
            tail.next = list1
        elif list2: 
            tail.next = list2

        return dummy.next

a2 = ListNode(2,None)
a1 = ListNode(1,a2)


b4 = ListNode(4,None)
b3 = ListNode(3,b4)
b1 = ListNode(1,b3)

s = Solution()
answer = s.mergeTwoLists(a1,b1)

pretty_answer = []
while answer:
    pretty_answer.append(answer.val)
    answer = answer.next
print(pretty_answer)