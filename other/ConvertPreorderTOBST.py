
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, A):
        dummy = TreeNode((1 << 31))
        stack = [dummy]
        for a in A:
            node = TreeNode(a)

            parent = None
            while stack[-1].val < a:
                parent = stack.pop()

            if not parent:
                stack[-1].left = node
            else:
                parent.right = node
            stack.append(node)

        return dummy.left

    def traverse(self, root):
        if not root:
            return

        print root.val
        self.traverse(root.left)
        self.traverse(root.right)


if __name__ == "__main__":
    s = Solution()

    s.traverse(s.getSolution([4, 2, 6, 7, 8]))
