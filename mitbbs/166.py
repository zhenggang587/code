import random

# insert, delete, random
class Solution:
    def __init__(self):
        self.arr = []
        self.m = {}

    def add(self, key):
        if key in self.m:
            return

        self.m[key] = len(self.arr)
        self.arr.append(key)

    def delete(self, key):
        if key not in self.m:
            return

        index = self.m[key]
        self.arr[index] = self.arr[-1]
        del self.m[key]
        self.arr.pop()

    def getRandom(self):
        k = random.randint(1, len(self.arr))
        return self.arr[k - 1]


if __name__ == "__main__":
    s = Solution()
    
    s.add(1)
    s.add(2)
    s.add(4)
    s.add(10)
    s.add(1111)
    print s.getRandom()
    print s.getRandom()
    print s.getRandom()
    print s.getRandom()
    s.delete(4)
    print s.getRandom()
    print s.getRandom()
    print s.getRandom()
