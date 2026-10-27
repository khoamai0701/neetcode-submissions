class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        maxProf = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                r += 1
                if profit > maxProf:
                    maxProf = profit
            else:
                l += 1
                r = l + 1
            
            
        
        return maxProf