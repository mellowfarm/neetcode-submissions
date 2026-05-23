class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq = {}
        heap = []
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res