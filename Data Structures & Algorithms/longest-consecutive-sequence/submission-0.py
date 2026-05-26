class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        res = 0

        def helper(num, unique_nums, size):
            if num + 1 in unique_nums:
                size += 1
                return helper(num + 1, unique_nums, size)
            return size
                

        for num in unique_nums:
            if num-1 not in unique_nums:
                seq_size = helper(num, unique_nums, 1)
                if seq_size > res:
                    res = seq_size
        
        return res

        
        
            

        
            


