class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        seen = {}
        subarrays = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            target = prefix_sum - k
            if target == 0:
                subarrays += 1
            if target in seen:
                subarrays += seen[target]
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
        
        return subarrays
            
        


        