class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heap_size = 0
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            heap_size += 1
            if heap_size > k:
                heapq.heappop(heap)
                heap_size -= 1
        
        while heap:
            v, k = heapq.heappop(heap)
            res.append(k)
        
        return res