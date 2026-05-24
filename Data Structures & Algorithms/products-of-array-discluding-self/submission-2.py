class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*(len(nums))
        right = [1]*(len(nums))
        curr_left = 1
        curr_right = 1
        res = [None] * len(nums)
        for i in range(len(nums)):
            left[i] = curr_left
            right[len(nums)-1-i] = curr_right
            curr_left *= nums[i]
            curr_right *= nums[len(nums)-1-i]
        for j in range(len(nums)):
            res[j] = left[j]*right[j]
        return res

            
        
        
