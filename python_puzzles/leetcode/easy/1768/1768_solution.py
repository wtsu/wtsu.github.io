#https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        #logic
        ### Alternate between words
        ### for each turn, pull out the respective letter and append to a variable
        ### once one of the words have been fully parsed through, get the reminaing letters in the other word and append


        #variable intialization

        #ans stores the appended results
        ans = ""

        #l1 and l2 store an index telling us what letter in the respective word to look at
        l1 = 0
        l2 = 0

        #used to tell how many times you have alternated between words
        count = 0

        #apply this logic as long as you haven't gone through either word completely
        while l1 < len(word1) and l2 < len(word2):

            #each loop you increment the counter
            #when the counter is even, that means you should look at word1
            if count %2 ==0:
                ans =  ans+word1[l1] #append the letter in word1
                l1+=1 #increment so the next loop you look at the next letter
            
            #when the counter is odd, that means you should look at word2
            elif count%2!=0:
                ans = ans+word2[l2] #append the letter in word2
                l2+=1 #incremennt so the next loop you look at the next letter
            count+=1
        
        #when the while loop breaks, that means you have gone through a word completely. now you just append the rest of the remaining word

        #you can know which word got parsed through by looking at the l1 and l2 variables. 
        #If the they are respectively less then the actual length of the word, you know you didn't fully go through the word
        if l1<len(word1):
            ans+=word1[l1:]
        if l2<len(word2):
            ans+=word2[l2:]

        return ans

s1 = Solution()

print(s1.mergeAlternately('apple','goat'))