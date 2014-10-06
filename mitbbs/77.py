import random

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.weight = 0
        self.left = None
        self.right = None

class WeightedNum:
    def __init__(self, x, w):
        self.val = x
        self.w = w

class Solution:
    def getSolution(self, p, k):
        root = self.traverse(p)
        ret = []
        for i in range(k):
            ret.append(self.getNum(root, random.random()))
        return ret

    def getNum(self, root, w):
        if not root.left and not root.right:
            return root.val

        if w <= root.left.weight:
            return self.getNum(root.left, w)
        else:
            return self.getNum(root.right, w - root.left.weight)

    def traverse(self, p):
        if len(p) == 1:
            leaf = TreeNode(p[0].val)
            leaf.weight = p[0].w
            return leaf

        root = TreeNode(0)
        mid = len(p) / 2
        root.left = self.traverse(p[:mid])
        root.right = self.traverse(p[mid:])
        root.weight = root.left.weight + root.right.weight
        return root


if __name__ == "__main__":
    s = Solution()
    
    p = []
    p.append(WeightedNum(10, 0.05))
    p.append(WeightedNum(120, 0.45))
    p.append(WeightedNum(30, 0.5))
    print s.getSolution(p, 10)
