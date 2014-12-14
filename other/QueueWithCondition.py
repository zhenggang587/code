import threading
import time
import random

class BlockingQueue:
    def __init__(self, capacity):
        self.q = [None for i in range(capacity + 1)]
        self.start = self.end = 0
        self.notFull = threading.Condition()
        self.notEmpty = threading.Condition()

    def enqueue(self, v):
        index = (self.end + 1) % len(self.q)
        self.notFull.acquire()
        while index == self.start:
            self.notFull.wait() 
            
        print 'put ', v
        self.q[self.end] = v
        self.end = index

        self.notFull.release()

        self.notEmpty.acquire()
        self.notEmpty.notify()
        self.notEmpty.release()

    def dequeue(self):
        self.notEmpty.acquire()
        while self.start == self.end:
            self.notEmpty.wait() 

        index = (self.start + 1) % len(self.q)
        tmp = self.q[self.start]
        self.start = index

        self.notEmpty.release()

        self.notFull.acquire()
        self.notFull.notify()
        self.notFull.

        print 'get ', tmp
        return tmp

class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self._stop = False

    def run(self):
        while not self._stop:
            val = random.randint(1, 5)
            self.queue.enqueue(val)
            time.sleep(val)

    def stop(self):
        self._stop = True

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self._stop = False

    def run(self):
        while not self._stop:
            val = random.randint(1, 5)
            self.queue.dequeue()
            time.sleep(val)

    def stop(self):
        self._stop = True


if __name__ == "__main__":
    q = BlockingQueue(2)

    p = Producer(q)
    c = Consumer(q)
    p.start()
    c.start()
    time.sleep(30)
    p.stop()
    c.stop()
        
