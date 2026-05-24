class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_pdt = 1
        num_zeros = 0
        res1 = [0]*len(nums)
        res2 = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros += 1
                continue
            total_pdt = total_pdt * nums[i]

        if num_zeros > 1:
                return res2
        
        for i in range(len(nums)):
            if nums[i] == 0:
                res2[i] = total_pdt
                return res2
            else:
                res1[i] = int(total_pdt / nums[i])
        return res1