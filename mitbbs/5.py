
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

INT_MAX = (1 << 31)

class Solution:
    def getSolution(self, root1, root2):
        ret = []
        f1 = iter(self.inorder(root1))
        f2 = iter(self.inorder(root2))
        v1, v2 = next(f1, INT_MAX), next(f2, INT_MAX)
        while v1 != INT_MAX or v2 != INT_MAX:
            if v1 < v2:
                ret.append(v1)
                v1 = next(f1, INT_MAX)
            else:
                ret.append(v2)
                v2 = next(f2, INT_MAX)
        return ret

    def inorder(self, root):
        if not root:
            yield INT_MAX 

        stack = []
        p = root
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                yield p.val
                p = p.right


if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node1.left = node3
    node3.right = node2

    node4 = TreeNode(0)
    print s.getSolution(node1, node4)
