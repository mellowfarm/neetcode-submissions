class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def generate(curr, num_open, num_close):
            if len(curr) == 2*n:
                res.append(curr)
            else:
                if num_open < n:
                    generate(curr+'(', num_open+1, num_close)
                if num_open > num_close:
                    generate(curr+')', num_open, num_close+1)
        
        generate('', 0, 0)
        return res
