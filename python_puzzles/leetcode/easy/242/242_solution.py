# https://leetcode.com/problems/valid-anagram/
#https://www.youtube.com/watch?v=9UtInBqnCgA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # create dictionary(eg Hashmap to store counts of letters)
        countS, countT = {},{}

        #go through string
        for i in range(len(s)):
            # use the get fn in case the key dne
            countS[i] = 1 + countS.get(s[i],0) 
            countT[i] = 1 + countT.get(t[i],0)

        #compare hashmaps
        for c in countS: 
            if countS.get(c,0) != countT.get(c,0):
                return False 
        return True
s1 = Solution()
print(s1.isAnagram('aab','baa'))