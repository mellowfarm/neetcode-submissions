class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque

        # translate to graph
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            curr_pair = prerequisites[i]
            graph[curr_pair[1]].append(curr_pair[0])
        
        # Kahn's algorithm
        in_degree = [0] * numCourses
        for key in graph:
            for k in range (len(graph[key])):
                in_degree[graph[key][k]] += 1
        
        queue = deque([x for x in range (numCourses) if in_degree[x] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for n in graph[node]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)
        
        return len(order) == numCourses;