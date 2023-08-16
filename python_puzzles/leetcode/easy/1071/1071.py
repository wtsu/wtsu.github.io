'''
redo #1
- careful with boolean conditions that come from modulo. it should be len(str1) % len(substring) and not len(substring) % len(str1)
'''
class Solution: 
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def isDivisor(substring, str1, str2):
            l = len(substring)
            l1, l2 = len(str1), len(str2)

            if l1 % l != 0 and l2 % l != 0:
                return False
            
            f1, f2 = int(l1/l), int(l2/l)

            if substring*f1 == str1 and substring*f2 == str2:
                return True 

            return False

        for l in range(max(len(str1),len(str2)), 0, -1):
            substring = str1[:l]
            if isDivisor(substring,str1, str2):
                return str1[:l]
        return ""
    
s1 = Solution()
print(s1.gcdOfStrings('LEET','CODE'))