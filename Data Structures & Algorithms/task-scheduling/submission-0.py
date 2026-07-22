class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        queue = []
        taskmap = {}
        time = 0
        num_popped = 0
        
        for task in tasks:
            taskmap[task] = taskmap.get(task, 0) + 1
        
        for task, freq in taskmap.items():
            heapq.heappush(maxheap, (-1*freq, task))
        
        while maxheap:
            round_tasks = 0
            for i in range(n+1):
                if maxheap:
                    freq, task = heapq.heappop(maxheap)
                    freq = -1*freq
                    num_popped += 1
                    round_tasks += 1
                    if freq - 1 > 0:
                        queue.append((-1*(freq-1), task))
            
            for q in queue:
                heapq.heappush(maxheap, q)
            queue = []
            
            if maxheap:
                time += n+1
            else:
                time += round_tasks
        
        return time

        

            

            

