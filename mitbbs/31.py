
class Iter:
    def __init__(self, count):
        self.count = count

    def hasNext(self):
        return self.count > 0

    def next(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

class IterWrapper:
    def __init__(self, count):
        self.iter = Iter(count)
        self.p = None

    def hasNext(self):
        return self.p or self.iter.hasNext()

    def next(self):
        if not self.p:
            self.p = self.peek() 
        r = self.p
        self.p = None

        return r

    def peek(self):
        if not self.p:
            self.p = self.iter.next()
        return self.p


if __name__ == "__main__":
    s = IterWrapper(10)
    
    print s.next()
    print s.next()
    print s.peek()
    print s.peek()
    print s.next()
    print s.next()
    print s.peek()
