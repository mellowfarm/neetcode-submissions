class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda interval: interval[0])
        curr = intervals[0]
        merged = []
        for interval in intervals:
            if curr[0] <= interval[0] and curr[1] >= interval[1]: 
                # interval overlap within current
                continue
            elif curr[0] <= interval[0] <= curr[1] and curr[1] < interval[1]:
                # interval overlap but longer than current so extend merge region
                curr = [curr[0], interval[1]]
            elif curr[1] == interval[0]:
                curr = [curr[0], interval[1]]
            else:
                merged.append(curr)
                curr = interval
        
        merged.append(curr)
        return merged
            
            