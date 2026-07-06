class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        curr_longest = 0
        left = 0
        right = 0
        seen = {}

        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left: # duplicate found
                left = seen[s[right]] + 1
            curr_longest = max(right-left+1, curr_longest)
            seen[s[right]] = right
            right += 1
            
        return curr_longest


        
