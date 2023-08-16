#https://leetcode.com/problems/design-hashmap/
#https://www.youtube.com/watch?v=cNWsgbKwwoU&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=6

class ListNode: 
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        #hashmap can have 1000 entries at most
        #creates those 1000 entries and adds an initial ListNode
        self.map = [ListNode() for i in range(1000)]

    def hash(self,key):
        #based on the key in the node, get back the index in the hashmap
        return key % len(self.map)


    def put(self, key: int, value: int) -> None:
        #points to the initial dummy node
        cur = self.map[self.hash(key)]

        while cur.next: #cur.next b/c we want to go all the way to the final pointer, not just the second to last one where next would be first null
            #keep on looking through the linked listnodes. If one of the listnodes already exist, then update the value
            if cur.next.key == key:
                cur.next.val = value
                return 
            cur = cur.next

        #creates the new list node
        cur.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next #since you don't need to start at the dummy node
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next: 
            if cur.next.key == key:
                #causing the matching node to get skipped thus "deleted"
                cur.next = cur.next.next
                return
            cur = cur.next 


key, value = 1,2
obj = MyHashMap()
obj.put(key,value)
param_2 = obj.get(key)
obj.remove(key)