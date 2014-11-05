
class Queue:
    def __init__(self):
        self.minq = []
        self.maxq = []
        self.q = []

    def push(self, val):
        self.q.append(val)

        while self.minq and self.minq[-1] > val:
            self.minq.pop()
        self.minq.append(val)

        while self.maxq and self.maxq[-1] < val:
            self.maxq.pop()
        self.maxq.append(val)

    def pop(self):
        if not self.q:
            return

        val = self.q.pop(0)
        if self.minq[0] == val:
            self.minq.pop(0)
        if self.maxq[0] == val:
            self.maxq.pop(0)

    def getMax(self):
        if not self.maxq:
            return None
        return self.maxq[0]

    def getMin(self):
        if not self.minq:
            return None
        return self.minq[0]
            

if __name__ == "__main__":
    q = Queue()

    q.push(3)
    q.push(-3)
    print q.getMax(), q.getMin()
    q.push(2)
    q.push(35)
    print q.getMax(), q.getMin()
    q.pop()
    q.push(0)
    q.pop()
    print q.getMax(), q.getMin()
    
