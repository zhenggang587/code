
# see 51nod/1153.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def getSolution(self, A):
        stack = []
        root = None
        for a in A:
            last = None
            '''
            it's MinTree
            '''
            while stack and stack[-1].val > a:
                last = stack.pop()

            node = TreeNode(a)
            node.left = last
            if not stack:
                root = node
            else:
                stack[-1].right = node
            stack.append(node)
        return root
                

if __name__ == "__main__":
    s = Solution()

    root = s.getSolution([3, 4, 5])
    print root.val
    print root.right.val
    print root.right.right.val

