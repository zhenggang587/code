class Solution:
    def init(self, n):
        self.d = [i for i in range(n)]
        self.r = [1 for i in range(n)]

    def find(self, i):
        if self.d[i] != i:
            self.d[i] = self.find(self.d[i])

        return self.d[i]

    def union(self, i, j):
        p = self.find(i)
        q = self.find(j)
        if p == q:
            return

        if self.r[p] >= self.r[q]:
            self.d[q] = p
            self.r[p] += self.r[q]
        else:
            self.d[p] = q
            self.r[q] += self.r[p]

    def findSuspect(self, n, groups):
        self.init(n)
        for group in groups:
            for i in range(1, len(group)):
                self.union(group[0], group[i])
        
        return self.r[self.d[0]]

        

if __name__ == "__main__":
    s = Solution()
     
    print s.findSuspect(100, [[1, 2], [10, 13, 11, 12, 14], [0, 1], [99, 2]])
