
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

INT_MAX = (1 << 31) 

class Solution:
    def __init__(self):
        self.stack = [[], []]
        self.p = [None, None]

    def getSolution(self, root1, root2):
        ret = []
        self.p = [root1, root2]
        val1 = self.inorder(0)
        val2 = self.inorder(1)
        while val1 != INT_MAX or val2 != INT_MAX:
            if val1 < val2:
                ret.append(val1)
                val1 = self.inorder(0)
            else:
                ret.append(val2)
                val2 = self.inorder(1)
        return ret

    def inorder(self, index):
        while self.stack[index] or self.p[index]:
            if self.p[index]:
                self.stack[index].append(self.p[index])
                self.p[index] = self.p[index].left
            else:
                self.p[index] = self.stack[index].pop()
                tmp = self.p[index].val
                self.p[index] = self.p[index].right
                return tmp
        return INT_MAX


if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node1.left = node3
    node3.right = node2

    node4 = TreeNode(0)
    print s.getSolution(node1, node4)
