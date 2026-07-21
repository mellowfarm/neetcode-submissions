class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.top = []

        self.nums.sort(reverse=True)

        if len(nums) >= k:
            for i in range(k):
                heapq.heappush(self.top, self.nums[i])
        else:
            for i in range(len(nums)):
                heapq.heappush(self.top, self.nums[i])
        
        self.curr_count = len(self.top)

    def add(self, val: int) -> int:
        if self.curr_count < self.k:
            heapq.heappush(self.top, val)
            self.curr_count += 1
        else:
            min_top_k = self.top[0]
            if val > min_top_k:
                popped = heapq.heappop(self.top)
                heapq.heappush(self.top, val)
        return self.top[0]
    


