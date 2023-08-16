from typing import List
#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #go in reverse order 
        #max = max(old_max,arr[i])

        old_max = -1 
        for i in range(len(arr)-1,-1,-1):
            new_max = max(old_max,arr[i]) #calculate the new max
            arr[i] = old_max #in first loop it will set it to -1, corresponding loops look at oldmax, which is the older max
            old_max = new_max #store the results of old max, so future runs can use it
        return arr
    
arr = [17,18,5,4,6,1]
s = Solution()
print(s.replaceElements(arr))