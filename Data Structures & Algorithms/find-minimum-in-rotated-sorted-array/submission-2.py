class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while True:
            if start == end:
                return nums[start]
            mid = int((start+end)/2)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[start] > nums[mid]:
                end = mid-1
            elif nums[end] < nums[mid]:
                start = mid+1
            else:
                return nums[0]

            
