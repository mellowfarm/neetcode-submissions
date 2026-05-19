class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]
        for i in range(1, len(intervals)):
            if sorted_intervals[i][0] == start or sorted_intervals[i][0] <= end :
                if sorted_intervals[i][1] > end:
                    end = sorted_intervals[i][1]
            else:
                if sorted_intervals[i][0] != start:
                    res.append([start, end])
                    start = sorted_intervals[i][0]
                    end = sorted_intervals[i][1]
        
        res.append([start, end])
        return res
