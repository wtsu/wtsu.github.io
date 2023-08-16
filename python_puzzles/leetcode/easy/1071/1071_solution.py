#https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
#https://www.youtube.com/watch?v=i5I_wrbUdzM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #get the length of each string
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            #is the length at least a divisor?
            if len1 % 1 or len2 % 1:
                return False
            
            #get the factor(eg:the number of times a "substring" would need to be replicated to create str1 and str2)
            f1, f2 = len1 // l, len2 // l

            #multiply this substring and see if it reconstitutes the target strings
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        #iterate through
        #range(start, stop, step) , this means that the iteration will go down to 0 at a increment of -1
        for l in range(min(len1,len2),0,-1):
            print(f'this is l : {l}')
            if isDivisor(l):
                return str1[:l]
        return ""
    
s1 = Solution()

print(s1.gcdOfStrings("gatgat","gat"))