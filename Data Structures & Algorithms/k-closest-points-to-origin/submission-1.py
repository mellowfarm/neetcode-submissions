class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        count = 0
        
        for i, point in enumerate(points):
            xp, yp = point[0], point[1]
            distances.append((xp*xp + yp*yp, i))
        
        heapq.heapify(distances)
        while count < k:
            dist, idx = heapq.heappop(distances)
            res.append(points[idx])
            count += 1

        return res