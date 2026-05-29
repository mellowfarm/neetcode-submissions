class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        max_num = nums_sorted[-1]
        res = []
        
        def search(start, end, nums, target):
            mid = (start + end) // 2
            if start > end:
                return None
            elif nums[mid] == target:
                return target
            elif start == end:
                return None
            elif nums[mid] > target:
                return search(start, mid-1, nums, target)
            else:
                return search(mid+1, end, nums, target)
        
        for i in range(len(nums_sorted)):
            curr = nums_sorted[i]
            leftover = 0 - curr
            
            for j in range(i+1, len(nums_sorted)):
                threesum = [curr]
                first = nums_sorted[j]
                target = leftover - first
                if target > max_num:
                    continue
                second = search(j+1, len(nums_sorted)-1, nums_sorted, target)
                if second is None:
                    continue
                else:
                    threesum.append(first)
                    threesum.append(second)
                
                if len(threesum) == 3:
                    if threesum in res:
                        continue
                    else: 
                        res.append(threesum)
        
        return res


