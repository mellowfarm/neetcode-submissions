class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
            else:
                while stack[-1][1] < temp:
                    k, popped_temp = stack.pop()
                    result[k] = i - k
                    if not stack:
                        break
                stack.append((i, temp))
        
        return result
