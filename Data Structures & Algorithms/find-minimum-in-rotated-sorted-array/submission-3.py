class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while True:
            mid = int((start+end)/2)
            if start == end:
                return nums[mid]
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid

            
