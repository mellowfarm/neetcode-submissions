class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_so_far = float('inf')
        best = 0
        for p in prices:
            if lowest_so_far > p:
                lowest_so_far = min(lowest_so_far, p)
                continue
            best = max(p-lowest_so_far, best)
        
        return best