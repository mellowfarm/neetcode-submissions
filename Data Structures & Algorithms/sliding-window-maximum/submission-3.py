class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        deque = deque()
        res = []
        for i, num in enumerate(nums):
            # remove stuff that isnt in the window
            while deque and deque[0] < i - k + 1:
                deque.popleft()
            
            while deque and nums[deque[-1]] < num:
                deque.pop()
            
            deque.append(i)

            if i >= k - 1:
                res.append(nums[deque[0]])

        return res
