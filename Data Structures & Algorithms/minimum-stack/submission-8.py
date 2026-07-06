class MinStack:

    def __init__(self):
        self.stk: List[tuple] = []
        self.currMin = float('inf')

    def push(self, val: int) -> None:
        self.currMin = min(self.currMin, val)
        self.stk.append((val, self.currMin))

    def pop(self) -> None:
        self.stk.pop()
        if self.stk:
            self.currMin = self.stk[-1][1]
        else:
            self.currMin = float('inf')
        

    def top(self) -> int:
        return self.stk[-1][0]
        

    def getMin(self) -> int:
        return self.stk[-1][1]
