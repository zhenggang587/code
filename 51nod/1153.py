
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, A):
        root = self.buildTree(A)
        return self.height(root)

    def buildTree(self, A):
        stack = []
        root = None
        for a in A:
            last = None
            while stack and stack[-1].val < a:
                last = stack.pop()

            node = TreeNode(a)
            node.left = last
            if not stack:
                root = node
            else:
                stack[-1].right = node
            stack.append(node)
        return root

    def height(self, root):
        if not root:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1



if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([9, 10, 2, -1, 3, -5, 0, -3, 1, 12, 5, 8, -2, 6, 4])
