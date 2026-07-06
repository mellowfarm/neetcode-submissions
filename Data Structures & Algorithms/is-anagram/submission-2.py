class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        if len(s_list) != len(t_list):
            return False

        s_dict = {}
        for char in s_list:
            s_dict[char] = s_dict.get(char, 0) + 1
        
        for char in t_list:
            if char not in s_dict:
                return False
            s_dict[char] -= 1 
        
        return all(v == 0 for v in s_dict.values())