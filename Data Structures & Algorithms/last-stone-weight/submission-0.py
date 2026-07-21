class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            if x < y:
                y = y - x
                heapq.heappush(stones, -1 * y)
                continue
            if y < x:
                x = x - y
                heapq.heappush(stones, -1 * x)
                continue
        
        if len(stones) == 1:
            return -1 * stones[0]
        else:
            return 0
