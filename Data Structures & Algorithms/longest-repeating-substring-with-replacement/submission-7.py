class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s = list(s)
        left = 0
        right = 0
        longest = 1
        chars = {}
        max_freq = 0
        while right < len(s):
            chars[s[right]] = chars.get(s[right], 0) + 1
            max_freq = max(max_freq, chars[s[right]])
            valid = right - left + 1 - max_freq <= k
            if valid:
                if right-left+1 > longest:
                    longest = right-left+1
                right += 1
            else:
                chars[s[left]] -= 1
                left += 1
                right += 1

        return longest
        