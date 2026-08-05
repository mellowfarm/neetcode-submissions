class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float("inf")
        max_profit = 0
        for price in prices:
            curr_min = min(price, curr_min)
            max_profit = max(max_profit, price-curr_min)
        
        return max_profit