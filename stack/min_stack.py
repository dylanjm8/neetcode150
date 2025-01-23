class MinStack:
    # Getting a min value in constant time requires a separate minimum stack to be popped from since popping is O(1)
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) # update minStack if this is a new minimum and if it is non empty
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        # This works because if a higher value number gets put on the stack then the minstack will simply repeat the previous minimum on its stack,
        # so it can be popped safely at the same time as stack
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
