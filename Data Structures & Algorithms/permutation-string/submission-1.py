class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1

        s2 = list(s2)
        s2_map = {}
        left = 0
        right = len(s1)-1
        for i in range(0, right):
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
        
        while right < len(s2):
            s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1
            if s1_map != s2_map:
                s2_map[s2[left]] = s2_map.get(s2[left], 0) - 1
                if s2_map[s2[left]] <= 0:
                    del s2_map[s2[left]]
                left += 1
                right += 1
            else:
                return True
        
        return False

            