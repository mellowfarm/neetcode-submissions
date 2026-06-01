class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        s = list(s)
        for i in range(len(s)):
            curr = 1
            seen = set()
            seen.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    if curr > longest:
                        longest = curr
                    break
                else:
                    curr += 1
                    seen.add(s[j])
            longest = max(longest, curr)
        
        return longest
