class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(target, row):
            start = 0
            end = len(row)-1
            mid = int((end+start)/2)
            while True:
                if row[mid] == target:
                    return True
                if start > end or start == end or start > len(row)-1 or end < 0:
                    return False
                if row[mid] > target:
                    end = mid-1
                    mid = int((end+start)/2)
                elif row[mid] < target:
                    start = mid+1
                    mid = int((end+start)/2)
        
        row_length = len(matrix[0])
        for r in range(len(matrix)):
            if matrix[r][0] <= target <= matrix[r][row_length-1]:
                return binary_search(target, matrix[r])
        
        return False
