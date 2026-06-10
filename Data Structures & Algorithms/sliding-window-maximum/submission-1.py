class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k-1
        res = []

        while right < len(nums):
            res.append(max(nums[left:right+1]))
            left += 1
            right += 1
        
        return res