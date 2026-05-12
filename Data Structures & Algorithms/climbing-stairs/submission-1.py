class Solution:
    def climbStairs(self, n: int) -> int:
    # ways to climb to stair n = # of ways to climb to stair n-1 + # of ways to climb to stair n-2
        memo = {}

        def helper(k):
            if k == 1:
                return 1
            if k == 2:
                return 2

            if k in memo:
                return memo[k]
            else:
                memo[k] = helper(k-1)+helper(k-2)
            
            return memo[k]

        return helper(n)  
        