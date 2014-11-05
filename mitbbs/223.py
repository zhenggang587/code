
class Base:
    def add(self):
        return

class Derived(Base):
    def __init__(self):
        self.cnt = 0

    def add(self):
        self.cnt += 1
        return Base.add(self)

    def counter(self):
        return self.cnt

if __name__ == "__main__":
    s = Derived()
    
    s.add()
    s.add()
    s.add()
    s.add()
    print s.counter()
