
class TreeNode:
    def __init__(self):
        self.left = self.right = self.mid = self.sum = 0

class Solution:
    def __init__(self, n):
        self.tree = [TreeNode() for i in range(n * 2 + 10)]
        self.buildTree(1, 1, n)

    def buildTree(self, num, l, r):
        self.tree[num].left = l
        self.tree[num].right = r 
        mid = (l + r) / 2
        self.tree[num].mid = mid

        if l < r:
            self.buildTree(2 * num, l, mid)
            self.buildTree(2 * num + 1, mid + 1, r)

    def insert(self, num, x, delta):
        if self.tree[num].left == x and self.tree[num].right == x:
            self.tree[num].sum += delta
            return

        if x <= self.tree[num].mid:
            self.insert(num * 2, x, delta)
        else:
            self.insert(num * 2 + 1, x, delta)
        self.tree[num].sum = self.tree[num * 2].sum + self.tree[num * 2 + 1].sum

    def query(self, num, l, r):
        if l <= self.tree[num].left and r >= self.tree[num].right:
            return self.tree[num].sum

        ans = 0
        if l <= self.tree[num].mid:
            ans += self.query(2 * num, l, r)
        if r > self.tree[num].mid:
            ans += self.query(2 * num + 1, l, r)
        return ans


if __name__ == "__main__":
    s = Solution(6)

    s.insert(1, 1, 4)
    s.insert(1, 2, 5)
    s.insert(1, 3, 6)
    s.insert(1, 4, 2)
    s.insert(1, 5, 1)
    s.insert(1, 6, 3)
    s.insert(1, 3, 5)
    print s.query(1, 1, 4)
    s.insert(1, 1, 9)
    print s.query(1, 2, 6)

