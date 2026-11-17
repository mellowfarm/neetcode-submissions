class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list((set(nums))))
        res = 0
        curr_longest = 1
        if len(nums) == 0:
            return res
        end = 1
        while end < len(nums):
            if nums[end] - nums[end-1] == 1:
                curr_longest += 1
            else:
                res = max(curr_longest, res)
                curr_longest = 1
            end += 1
        return max(curr_longest, res)
