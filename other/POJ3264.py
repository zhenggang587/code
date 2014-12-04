
class TreeNode:
    def __init__(self):
        self.left = self.right = self.mid = 0
        self.min = self.max = 0

INT_MAX = (1 << 31)
INT_MIN = -(1 << 31)
class Solution:
    def __init__(self):
        self.tree = [TreeNode() for i in range(2 * 100000 + 1)]

    def buildTree(self, index, A, l, r):
        if l > r:
            return (INT_MAX, INT_MIN)
        self.tree[index].left = l
        self.tree[index].right = r
        mid = (l + r) / 2
        self.tree[index].mid = mid
        if l == r:
            self.tree[index].min = self.tree[index].max = A[l - 1]
            return (A[l - 1], A[l - 1])

        (minl, maxl) = self.buildTree(2 * index, A, l, mid)
        (minr, maxr) = self.buildTree(2 * index + 1, A, mid + 1, r)
        self.tree[index].min = min(minl, minr)
        self.tree[index].max = max(maxl, maxr)
        return (self.tree[index].min, self.tree[index].max)

    def query(self, index, l, r):
        min, max = self._query(index, l, r)
        return max - min

    def _query(self, index, l, r):
        if l <= self.tree[index].left and r >= self.tree[index].right:
            return (self.tree[index].min, self.tree[index].max)

        minRet, maxRet = INT_MAX, INT_MIN
        if l <= self.tree[index].mid:
            minl, maxl = self._query(2 * index, l, r)
            minRet = min(minRet, minl)
            maxRet = max(maxRet, maxl)
        if r > self.tree[index].mid:
            minr, maxr = self._query(2 * index + 1, l, r)
            minRet = min(minRet, minr)
            maxRet = max(maxRet, maxr)
        return minRet, maxRet
            

if __name__ == "__main__":
    s = Solution()

    A = [1, 7, 3, 4, 2, 5]
    s.buildTree(1, A, 1, len(A))

    print s.query(1, 1, 5)
    print s.query(1, 4, 6)
    print s.query(1, 2, 2)

