class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from operator import add, sub, mul, truediv

        stack = []
        idx = 0
        mappings = {'+': add, '-': sub, '*': mul, '/': truediv}
    
        while idx < len(tokens):
            next_token = tokens[idx]
            if next_token in mappings:
                op = mappings[next_token]
                second = stack.pop()
                first = stack.pop()
                stack.append(int(op(first, second)))
            else:
                stack.append(int(next_token))
            
            idx += 1
        
        return stack[0]
            