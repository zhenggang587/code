import random

class Solution:
    def __init__(self):
        self.v = []
        self.m = {}

    def add(self, val, weight):
        if val not in self.m:
            self.m[val] = len(self.v)
            self.v.append([0, 0, val])

        idx = self.m[val]
        weight_diff = weight - self.v[idx][1] 
        self.v[idx][1] = weight
        self.adjust(idx, weight_diff)

    def remove(self, val):
        if val not in self.m:
            return

        idx = self.m[val]
        w = self.v[idx][1]
        n = len(self.v)
        if idx != n - 1:
            self.v[idx][2] = self.v[n - 1][2]
            self.v[idx][1] = self.v[n - 1][1]
            self.m[self.v[idx][2]] = idx
            weight_diff = self.v[n - 1][0] - w
            self.adjust(idx, weight_diff)

        weight_diff = -self.v[n - 1][0]
        self.adjust(n - 1, weight_diff)
        self.v.pop()
        del self.m[val]

    def adjust(self, idx, weight_diff):
        i = idx
        while i >= 0:
            self.v[i][0] += weight_diff
            i = (i - 1) >> 1

    def select(self):
        if not self.v:
            return None

        k = random.randint(1, self.v[0][0])
        i = 0
        n = len(self.v)
        while i < n:
            k -= self.v[i][1]
            if k <= 0:
                return self.v[i][2]
            i = i * 2 + 1
            if i < n and k > self.v[i][0]:
                i += 1
                k -= self.v[i][0]



if __name__ == "__main__":
    s = Solution()
    
    s.add(10, 4)
    s.add(120, 4)
    s.add(30, 4)
    for i in range(10):
        print s.select()
