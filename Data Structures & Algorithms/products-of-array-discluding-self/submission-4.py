class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        # right pass 
        right_running = 1
        for i in range(len(nums)-1):
            products[i+1] = nums[i] * right_running
            right_running *= nums[i]

        # left pass
        left_running = 1
        for j in range(len(nums)-1, 0, -1):
            products[j-1] *= nums[j] * left_running
            left_running *= nums[j]
        
        return products