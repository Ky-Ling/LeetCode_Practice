class minStack:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        val = min(val, self.minStack[-1]) if self.minStack else val
        self.minStack.append(val)


    def pop(self) -> int:
        self.stack.pop()
        self.minStack.pop()

    def getMin(self) -> int:
        return self.minStack[-1]

        