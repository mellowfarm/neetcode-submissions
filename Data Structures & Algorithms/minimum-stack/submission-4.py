class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []
        self.curr_min = None

    def push(self, val: int) -> None:
        if self.curr_min is None:
            self.curr_min = val
        else:
            if val < self.curr_min:
                self.curr_min = val

        self.stack.append(val)
        self.stack_min.append(self.curr_min)

    def pop(self) -> None:
        popped = self.stack.pop()
        self.stack_min.pop()

        if self.curr_min == popped:
            if self.stack_min:
                self.curr_min = self.stack_min[-1]
            else:
                self.curr_min = None


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min
