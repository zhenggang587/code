
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.queue = []

    def getSolution(self, root, key, m):
        if m == 0:
            return None
        self.inorder(root, key, m)
        return self.queue

    def inorder(self, root, key, m):
        if not root:
            return

        self.inorder(root.left, key, m)
        if len(self.queue) < m:
            self.queue.append(root)
        else:
            node = self.queue[0]
            if abs(node.val - key) >= abs(root.val - key):
                self.queue.pop(0)
                self.queue.append(root)
            else:
                return

        self.inorder(root.right, key, m)

    def printNode(self, node):
        for i in node:
            print i.val

if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node1.left = node3
    node3.right = node2

    node4 = TreeNode(4)
    node1.right = node4
    ret = s.getSolution(node1, 3, 3)
    s.printNode(ret)
