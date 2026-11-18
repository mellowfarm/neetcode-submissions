class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        right = 0
        s = list(s)
        longest = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= left: # inside the window
                longest = max(longest, right - left)
                left = seen[char] + 1
            seen[char] = i
            right += 1

        return max(longest, right - left)
                


        



