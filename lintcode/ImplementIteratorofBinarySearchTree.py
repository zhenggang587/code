
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.p = root

    #@return: True if there has next node, or false
    def hasNext(self):
        return self.stack or self.p

    #@return: return next node
    def next(self):
        if not self.hasNext():
            return None

        while self.stack or self.p:
            if self.p:
                self.stack.append(self.p)
                self.p = self.p.left
            else:
                tmp = self.stack.pop()
                self.p = tmp.right
                return tmp


if __name__ == "__main__":
    node1 = TreeNode(10)
    node2 = TreeNode(1)
    node3 = TreeNode(11)
    node4 = TreeNode(6)
    node5 = TreeNode(12)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.right = node5

    s = Solution(node1)
    while s.hasNext():
        print s.next().val
