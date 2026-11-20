class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        finished = 0

        # topological sorting 
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        for c, pr in prerequisites:
            graph[pr].append(c)
            in_degree[c] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            finished += 1
            for n in graph[curr]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)
        
        return finished == numCourses
            


        