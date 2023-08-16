'''
redo #1
- pay attention to the boolean condition when to stop going through words. w1 < len(word1) and w2 < len(word2) 
- don't forget to increment index pointers
'''

#https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def mergeAlternately(self, word1, word2):
        ans = ""

        w1 = 0
        w2 = 0

        turn = 0

        while w1 < len(word1) and w2 < len(word2):
            if turn%2 == 0: 
                ans = ans + word1[w1]
                w1 += 1
            else:
                ans = ans + word2[w2]
                w2 += 1
            turn += 1
        
        if w1 < len(word1):
            ans = ans + word1[w1:]
        
        if w2 < len(word2):
            ans = ans + word2[w2:]

        return ans

s1 = Solution()

print(s1.mergeAlternately('a','1234'))