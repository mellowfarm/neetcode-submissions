class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)

        if len(s) < len(t):
            return ""

        curr_window = len(t)
        left = 0
        right = curr_window
        while curr_window <= len(s):
            curr = s[left:right]
            if Counter(t) <= Counter(curr):
                return "".join(curr)
            else:
                if right+1 > len(s):
                    curr_window += 1
                    left = 0
                    right = curr_window
                else:
                    left += 1
                    right += 1
        
        return ""
            


