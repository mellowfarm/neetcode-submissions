class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph
        graph = defaultdict(list)
        for p in prerequisites:
            course, prereq = p[0], p[1]
            graph[prereq].append(course)
        
        # topological sort
        in_degree = [0] * numCourses
        for course in range(numCourses):
            for neighbour in graph[course]:
                in_degree[neighbour] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbour in graph[curr]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(order) == numCourses:
            return order
        else:
            return []
        
        

            
        