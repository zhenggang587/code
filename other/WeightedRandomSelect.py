
class Solution:
    def __init__(self):
        self.arr = []
        self.map = {}

    
    def search(self, k):
        return k in self.map

    def insert(self, k, weight):
        if k not self.map:
            self.map[k] = len(self.arr)
            self.arr.append([k, 0, weight])

        idx = self.map[k]
        weight_diff = self.weight - self.arr[idx][2]
        self.arr[idx][2] = weight
        i = idx
        while i >= 0:
            self.arr[i][1] += weight_diff
            i = (i - 1) >> 1


    def delete(self, k):
        if k not in self.map:
            return

        idx = self.map[k]
        size = len(self.arr)
        w = self.arr[idx][2]
        if idx != size - 1:
            weight_diff = self.arr[size - 1][2] - self.arr[idx][2]
            self.arr[idx][2] = self.arr[size - 1][2]
            self.arr[idx][0] = self.arr[size - 1][0]
            self.map[self.arr[idx][0]] = idx
            i = idx
            while i >= 0:
                self.arr[i][1] += weight_diff
                i = (i - 1) >> 1

        weight_diff = -self.arr[size - 1][2]
        i = size - 1
        while i >= 0:
            self.arr[i][1] += weight_diff
            i = (i - 1) >> 1
        self.arr.pop()
        del self.map[k]

    def random(self):
        if not self.arr:
            return None

        r = random.randint(1, self.arr[0][1])
        i = 0
        while i < len(self.arr):
            r -= self.arr[i][2]
            if r <= 0:
                return self.arr[i][0]
            i = 2 * i + 1
            if i < n and r > self.arr[i][1]:
                r -= self.arr[i][1]
                i += 1
        return None



            
