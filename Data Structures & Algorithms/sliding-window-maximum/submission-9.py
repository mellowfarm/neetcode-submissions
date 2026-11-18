class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        left = 0
        right = 0

        while right < len(nums):
            if len(heap) >= k: # window size reached
                curr_max = -heap[0]
                res.append(curr_max)
                if nums[left] == curr_max: # max value has left the window
                    while len(heap) > 0 and -heap[0] not in nums[left+1:right]:
                        heapq.heappop(heap)
                left += 1
                
            heapq.heappush(heap,-nums[right])
            right += 1
        
        res.append(-heap[0])
        return res
        
            

