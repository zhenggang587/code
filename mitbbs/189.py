
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.dist = (1 << 31) - 1
        self.ans = None

    def getSolution(self, root, k):
        if not root:
            return None

        self.getSolution(root.left, k)
        if pre and pre.val <= k and k <= root.val:
            return xx

        pre = root
        self.getSolution(root.right, k)
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
