class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        s = list(s)
        seen = {}

        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left: # duplicate
                curr = right - left
                if curr > longest:
                    longest = curr
                left = seen[s[right]] + 1
            else:
                seen[s[right]] = right
                right += 1
        
        return max(longest, right-left)
