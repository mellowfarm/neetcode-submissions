class Solution:
    def climbStairs(self, n: int) -> int:
        # state: dp[i] = number of distinct ways to climb i steps
        # recurrence: dp[i] = dp[i-1] + dp[i-2]
        # base: dp[0] = 1, dp[1] = 1
        # answer: dp[n]

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
