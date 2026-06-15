class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = int((end+start)/2)
        while True:
            if nums[mid] == target:
                return mid
            if start > end or start == end or start > len(nums)-1 or end < 0:
                return -1
            if nums[mid] > target:
                end = mid-1
                mid = int((end+start)/2)
            elif nums[mid] < target:
                start = mid+1
                mid = int((end+start)/2)
        