class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        curr_max = -1
        
        for i, rect in enumerate(heights):
            start = i
            while stack and rect < stack[-1][1]:
                popped_i, popped_rect = stack.pop()
                curr_max = max(curr_max, popped_rect*(i-popped_i))
                start = popped_i
            stack.append((start,rect))
        
        for popped_i, popped_rect in stack:
            curr_max = max(curr_max, popped_rect*(len(heights)-popped_i))
        
        return curr_max
        


                