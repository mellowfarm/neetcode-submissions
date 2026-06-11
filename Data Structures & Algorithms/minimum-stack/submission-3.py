class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = None

    def push(self, val: int) -> None:
        if self.curr_min is None:
            self.curr_min = val
        else:
            if val < self.curr_min:
                self.curr_min = val

        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.curr_min == popped:
            if self.stack:
                self.curr_min = min(self.stack)
            else:
                self.curr_min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min
