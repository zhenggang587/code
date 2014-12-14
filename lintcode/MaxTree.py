
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
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

    def traverse(self, root):
        if not root:
            return 

        print root.val
        self.traverse(root.left)
        self.traverse(root.right)


if __name__ == "__main__":
    s = Solution()

    root = s.maxTree([2, 5, 6, 0, 3, 1])
    s.traverse(root)
