#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=7
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit,maxProfit)
            else: #this only can happen if you just found a better buy price
                l = r
            r += 1
        return maxProfit

s = Solution()

prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
