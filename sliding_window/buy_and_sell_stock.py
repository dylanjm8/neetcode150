class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window -> two pointers right beside left, moving together as a window forcasting price change
        # one buy and one sell , if l < r, leave left pointer behind
        # time is key, cant go back to previous high
        # O(n) time, only one array run through

        l = 0 # buy
        r = 1 # sell
        
        max_profit = 0

        while r<len(prices):
            if prices[l] < prices[r]: # price increase
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit) # good way to update a potential max or min
            else: #not profitable or decrease
                l = r # shift all the way to the low price (where right is the min)
            r += 1

        return max_profit

        
        
