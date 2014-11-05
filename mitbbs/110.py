
class Solution:
    def __init__(self, pairs):
        self.pairs = pairs
        self.nindex = 0
        self.pindex = 0

    def hasNext(self):
        return self.nindex < len(self.pairs) and self.pindex < self.pairs[self.nindex][1]

    def next(self):
        if not self.hasNext():
            return

        tmp = self.pairs[self.nindex][0]
        self.pindex += 1
        if self.pindex >= self.pairs[self.nindex][1]:
            self.nindex += 1
            self.pindex = 0
        return tmp

if __name__ == "__main__":
    s = Solution([(1, 2), (2, 2), (4, 4)])

    while s.hasNext():
        print s.next()
