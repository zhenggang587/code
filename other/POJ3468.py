
class TreeNode:
    def __init__(self):
        self.left = self.right = self.mid = self.sum = 0

class Solution:
    def __init__(self):
        self.tree = [TreeNode() for i in range(2 * 100000 + 1)]
    
    def buildTree(self, index, A, l, r):
        if l > r:
            return 0
        self.tree[index].left = l
        self.tree[index].right = r
        mid = (l + r) / 2
        self.tree[index].mid = mid
        if l == r:
            self.tree[index].sum = A[l - 1]
            return A[l - 1]

        sum = self.buildTree(2 * index, A, l, mid)
        sum += self.buildTree(2 * index + 1, A, mid + 1, r)
        self.tree[index].sum = sum
        return sum

    def query(self, index, l, r):
        if l <= self.tree[index].left and r >= self.tree[index].right:
            return self.tree[index].sum

        sum = 0
        if l <= self.tree[index].mid:
            sum += self.query(2 * index, l, r)
        if r > self.tree[index].mid:
            sum += self.query(2 * index + 1, l, r)
        return sum

    def add(self, index, l, r, x):
        if l > r:
            return
        if self.tree[index].left == l and self.tree[index].right == l:
            self.tree[index].sum += x
            return

        if l <= self.tree[index].mid:
            self.add(2 * index, l, min(r, self.tree[index].mid), x)
        if r > self.tree[index].mid:
            self.add(2 * index + 1, max(l, self.tree[index].mid + 1), r, x)
        self.tree[index].sum = self.tree[2 * index + 1].sum + self.tree[2 * index].sum

if __name__ == "__main__":
    s = Solution()

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s.buildTree(1, A, 1, len(A))

    print s.query(1, 4, 4)
    print s.query(1, 1, 10)
    print s.query(1, 2, 4)
    s.add(1, 3, 6, 3)
    print s.query(1, 2, 4)
