class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in sums:
                return [sums[val], i]
            if num not in sums:
                sums[num] = i
            


            