class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s = list(s)
        left = 0
        right = 0
        longest = 1
        while right < len(s):
            chars = {}
            max_freq = 1
            for i in range(left, right+1):
                if s[i] in chars:
                    chars[s[i]] += 1
                    if chars[s[i]] > max_freq:
                        max_freq = chars[s[i]]
                else:
                    chars[s[i]] = 1
            valid = right - left + 1 - max_freq <= k
            if valid:
                if right-left+1 > longest:
                    longest = right-left+1
                right += 1
            else:
                left += 1

        return longest
        