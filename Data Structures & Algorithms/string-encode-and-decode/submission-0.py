class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            num_chars = len(strs[i])
            encoded_string += f"{num_chars}#{strs[i]}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        curr_str = s
        i = 0
        j = 0
        while i < len(s):
            if s[i] == '#':
                jump_by = int(s[j:i])
                word = s[i+1:i+jump_by+1]
                decoded_strs.append(word)
                i = i + jump_by + 1
                j = i
            else:
                i += 1
                
        return decoded_strs
                
