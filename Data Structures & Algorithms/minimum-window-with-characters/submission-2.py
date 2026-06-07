class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)

        if len(s) < len(t):
            return ""

        left = 0
        right = len(t)-1
        best_left = None
        best_right = None
        
        counter_t = Counter(t)
        
        counter_s = Counter(s[left:right+1])

        # find substring
        while right < len(s):
            if counter_t <= counter_s:
                if best_left is None or right - left < best_right - best_left:
                    best_left = left
                    best_right = right
                counter_s[s[left]] -= 1
                left += 1
            else:
                if right+1 < len(s):
                    right += 1
                    counter_s[s[right]] += 1
                else:
                    break
        
        if best_left is None and best_right is None:
            return ""
        else:
            return "".join(s[best_left:best_right+1])
            


