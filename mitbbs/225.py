import heapq
import threading
import time

class Timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.h = []
        self.stop = False

    def register(self, interval, func):
        heapq.heappush(self.h, (int(time.time()) + interval, interval, func))

    def run(self):
        while not self.stop:
            while self.h:
                triggertime, i, f = self.h[0]
                now = int(time.time())
                if triggertime < now:
                    heapq.heappop(self.h)
                elif triggertime == now:
                    f()
                    heapq.heappop(self.h)
                    heapq.heappush(self.h, (triggertime + i, i, f))
                else:
                    break

            time.sleep(1)

    def exit(self):
        self.stop = True
        
def f():
    print time.time()

def g():
    print "g", time.time()
        

if __name__ == "__main__":
    t = Timer()

    t.start()
    t.register(3, f)
    t.register(6, g)
    time.sleep(15)
    t.exit()
