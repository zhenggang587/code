import time

class webcounter:
    def __init__(self):
        self.minq = []
        self.mincnt = 0

    def increment(self):
        now = int(time.time())
        self.minq.append((now, 1))
        self.mincnt += 1

    def lastmin(self):
        now = int(time.time())
        while self.minq:
            if now - self.minq[0][0] < 60:
                break
            self.mincnt -= self.minq[0][1]
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
