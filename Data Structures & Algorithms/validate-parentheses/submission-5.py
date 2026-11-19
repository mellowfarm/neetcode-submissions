class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '[':']', '{':'}'}

        for b in s:
            if b in brackets:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if b != brackets[curr]:
                    return False
        
        return len(stack) == 0
            




        
            