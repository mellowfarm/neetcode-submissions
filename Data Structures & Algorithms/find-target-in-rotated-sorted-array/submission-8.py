class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while True:
            mid = int((start + end)/2)
            if nums[mid] == target:
                return mid
            if start > end:
                return -1
            
            # front 1/2 is sorted 
            if nums[mid] > nums[end]:
                # target is within sorted half
                if nums[start] <= target < nums[mid]: 
                    # find infront
                    end = mid-1
                else:
                    # find back
                    start = mid+1
            else:
                # target is within sorted half
                if nums[mid] < target <= nums[end]:
                    # find back
                    start = mid+1
                else:
                    end = mid-1
                        
