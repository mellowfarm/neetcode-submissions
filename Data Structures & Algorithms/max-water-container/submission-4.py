class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        first = 0
        second = len(heights)-1

        while first < second:
            vol = min(heights[first], heights[second]) * (second-first)
            if vol > max_vol:
                max_vol = vol
            if heights[first] < heights[second]:
                first += 1
            else:
                second -= 1

        return max_vol