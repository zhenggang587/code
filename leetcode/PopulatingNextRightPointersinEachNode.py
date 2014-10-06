
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        queue = []
        queue.append(root)
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                if len(queue) > 0 and i != l - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def traverse(self, node):
        if node.next:
            print node.val, node.next.val
        else:
            print node.val, None
        
        if node.left:
            self.traverse(node.left)
        if node.right:
            self.traverse(node.right)
        
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    s.connect(node1)

    s.traverse(node1)
