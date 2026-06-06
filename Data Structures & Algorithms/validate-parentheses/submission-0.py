class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)
        mapping = {'(':')', '{':'}', '[':']'}
        open_brackets = [k for k, v in mapping.items()]

        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if mapping[curr] != bracket:
                    return False
        
        return len(stack) == 0