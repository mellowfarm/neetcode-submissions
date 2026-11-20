class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state: dp[i] = fewest number of coins for amount i
        # recurrence: for c <= i: dp[i] = min(dp[i-c]+1)
        # base: dp[0] = 0
        # answer: dp[amount]

        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        if dp[amount] == float("inf"):
            return -1
        
        return dp[amount]