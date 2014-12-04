
# lowest common ancestor
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.p = None
        self.q = None

    def getSolution(self, root, n1, n2):
        if not root:
            return None

        if root.val == n1 or root.val == n2:
            return root

        leftLca = self.getSolution(root.left, n1, n2)
        rightLca = self.getSolution(root.right, n1, n2)
        if leftLca and rightLca:
            return root

        return leftLca if leftLca else rightLca
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
