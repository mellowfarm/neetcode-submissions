class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        left = 0
        right = 0

        while right < len(nums):
            if len(heap) >= k: # window size reached
                while heap[0][1] < left:
                    heapq.heappop(heap)
                curr_max = -heap[0][0]    
                res.append(curr_max)
                left += 1    
            heapq.heappush(heap,(-nums[right], right))
            right += 1
        
        while heap[0][1] < left:
            heapq.heappop(heap)
        res.append(-heap[0][0])
        return res
        
            

