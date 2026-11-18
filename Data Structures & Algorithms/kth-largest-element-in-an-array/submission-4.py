class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        largest = 0

        while k > 0:
            largest = -heapq.heappop(heap)
            k -= 1
        
        return largest




            