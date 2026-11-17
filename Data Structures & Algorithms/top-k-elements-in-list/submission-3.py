class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        heap = []
        res = []
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        for num, freq in frequency.items():
            heapq.heappush(heap, (-1 * freq, num))
        
        while k > 0:
            freq, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        
        return res