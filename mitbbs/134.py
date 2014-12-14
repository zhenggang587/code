import time

class webcounter:
    def __init__(self):
        self.minq = []
        self.minMap = {}
        self.mincnt = 0

    def increment(self):
        now = int(time.time())
        if now in self.minMap:
            index = self.minMap[now]
            self.minq[index][1] += 1
        else:
            self.minMap[now] = len(self.minq)
            self.minq.append([now, 1])
        self.mincnt += 1

    def lastmin(self):
        now = int(time.time())
        while self.minq:
            if now - self.minq[0][0] < 60:
                break
            self.mincnt -= self.minq[0][1]
            del self.minMap[self.minq[0][0]]
            self.minq.pop(0)

        return self.mincnt


if __name__ == "__main__":
    s = webcounter()
    
    s.increment()
    s.increment()
    s.increment()
    s.increment()
    s.increment()
    print s.lastmin()
