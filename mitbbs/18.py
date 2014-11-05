
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, preorder, inorder):
        if not preorder:
            return None

        val = preorder[0]
        index = inorder.index(val)
        root = TreeNode(val)

        root.left = self.getSolution(preorder[1:index + 1], inorder[:index])
        root.right = self.getSolution(preorder[index + 1:], inorder[index + 1:])
        return root

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
