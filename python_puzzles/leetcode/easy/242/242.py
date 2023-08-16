class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {},{}

        if len(s) != len(t):
            return False 
        
        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for c in countS: 
            if countS.get(c) != countT.get(c):
                return False
        return True
    
s1 = Solution()
print(s1.isAnagram('rat','car'))