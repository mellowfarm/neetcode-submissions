class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        curr_length = 1
        if len(nums) == 0:
            return longest
        for num in nums:
            if num - 1 not in nums: # start of sequence
                curr = num
                while curr + 1 in nums:
                    curr_length += 1
                    curr = curr + 1
                longest = max(curr_length, longest)
                curr_length = 1
        return longest
