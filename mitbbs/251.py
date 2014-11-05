
class TreeNode:
    def __init__(self):
        self.left = self.right = self.mid = 0
        self.minVal = 0

class Solution:
    def __init__(self, A):
        n = len(A)
        self.tree = [TreeNode() for i in range(n * 2 + 10)]
        self.buildTree(1, 0, n - 1)
        for i in range(n):
            self.insert(1, i, A[i])

    def buildTree(self, index, l, r):
        self.tree[index].left = l
        self.tree[index].right = r
        m = l + (r - l) / 2
        self.tree[index].mid = m

        if l < r:
            self.buildTree(2 * index, l, m)
            self.buildTree(2 * index + 1, m + 1, r)

    def insert(self, index, x, val):
        if self.tree[index].left == x and self.tree[index].right == x:
            self.tree[index].minVal = val
            return

        if x <= self.tree[index].mid:
            self.insert(index * 2, x, val)
        else:
            self.insert(index * 2 + 1, x, val)

        self.tree[index].minVal = min(self.tree[index *2].minVal, self.tree[index * 2 + 1].minVal)

    def query(self, index, l, r):
        if l <= self.tree[index].left and r >= self.tree[index].right:
            return self.tree[index].minVal

        ans = (1 << 31)
        if l <= self.tree[index].mid:
            ans = min(ans, self.query(2 * index, l, r))
        if r > self.tree[index].mid:
            ans = min(ans, self.query(2 * index + 1, l, r))
        return ans

if __name__ == "__main__":
    s = Solution([4, 1, 3, 2])
    
    print s.query(1, 0, 4)
    print s.query(1, 2, 3)
    print s.query(1, 0, 0)
