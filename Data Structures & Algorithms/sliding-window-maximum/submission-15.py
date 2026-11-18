class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if a bigger number arrives before a smaller number the smaller number 
        # will never be a max value so we can js pop it

        dq = deque([])
        res = []

        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k: # within the window
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
            


            
        
            

