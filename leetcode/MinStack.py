
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
        return x

    # @return nothing
    def pop(self):
        if not self.stack:
            return

        x = self.stack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()

    # @return an integer
    def top(self):
        if not self.stack:
            return None

        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if not self.minStack:
            return None

        return self.minStack[-1]
        
if __name__ == "__main__":
    s = MinStack()

    s.push(3)
    s.push(1)
    s.push(2)
    print s.top()
    print s.getMin()
    s.pop()
    print s.top()
    print s.getMin()

