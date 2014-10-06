
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0

        queue = []
        queue.append(root)
        level = 0
        while queue:
            l = len(queue)
            level += 1
            for i in range(l):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return level
        return level


if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(1)
    #node1.left = node2
    #node1.right = node3
    node2.left = node4
    #node3.left = node5
    #node3.right = node6
    node4.left = node7
    node4.right = node8
    #node6.right = node9

    print s.minDepth(node1)
