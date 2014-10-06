
class Set:
    def __init__(self):
        self.map = {}
        self.data = []
        self.len = 0

    def insert(self, val):
        if val in self.map:
            return

        self.map[val] = self.len
        if self.len < len(self.data):
            self.data[self.len] = val
        else:
            self.data.append(val)
        self.len += 1

    def delete(self, val):
        if val not in self.map:
            return

        pos = self.map[val]
        self.data[pos], self.data[self.len - 1] = self.data[self.len - 1], self.data[pos]
        self.len -= 1
        del self.map[val]

    def random(self, k):
        return self.data[k - 1]

if __name__ == "__main__":
    s = Set()
    
    s.insert(1)
    s.insert(2)
    s.insert(3)
    print s.random(2)
    s.delete(2)
    print s.random(2)

