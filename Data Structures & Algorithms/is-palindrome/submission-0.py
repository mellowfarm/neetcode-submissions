class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [char.lower() for char in s if char.isalnum()]
        reverse_s_list = s_list[::-1]

        for i in range(len(s_list)):
            if s_list[i] != reverse_s_list[i]:
                return False
            
        return True