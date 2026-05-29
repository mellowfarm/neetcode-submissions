class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        res = []

        for i in range(len(nums_sorted)):
            left, right = i+1, len(nums_sorted)-1
            
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue

            while left < right:
                curr = nums_sorted[i]
                first = nums_sorted[left]
                second = nums_sorted[right]

                total_sum = curr + first + second

                if total_sum == 0:
                    res.append([curr, first, second])
                    left += 1
                    right -= 1
                    while left < right and nums_sorted[left] == nums_sorted[left-1]:
                        left += 1
                elif total_sum > 0:
                    right -= 1
                elif total_sum < 0:
                    left += 1
            
        return res
                    