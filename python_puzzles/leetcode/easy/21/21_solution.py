from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node that this always start with
        dummy = ListNode()

        #tail helps point to the node we want to be modifying
        tail = dummy
        while list1 and list2: #comparisons are only possible if both exist
            if list1.val < list2.val: #if the list1 val is lower, modify the tail node to point to the list1 node
                tail.next = list1
                list1 = list1.next #increment list1 to the next node in that linked list
            else: #this conditions means list2 is the next sequential. Modify the tail node to point to the list2 node
                tail.next = list2 
                list2 = list2.next #increment list2 to the next node
            tail = tail.next
        

        #once at least one of the linked lists are done, go determine which is remaining and just add it in
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