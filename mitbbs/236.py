
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root1, root2):
        hasVisited = set()
        return self.traverse(root1, root2, hasVisited)

    def traverse(self, root1, root2, hasVisited):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        if root1 in hasVisited:
            return True

        isSame = root1.val == root2.val and self.traverse(root1.left, root2.left, hasVisited) \
            and self.traverse(root1.right, root2.right, hasVisited)
        if isSame:
            hasVisited.add(root1)
        return isSame

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node8 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node2.right = node8
    node3.left = node8

    node4 = TreeNode(1)
    node5 = TreeNode(2)
    node6 = TreeNode(2)
    node7 = TreeNode(3)
    node4.left = node5
    node4.right = node6
    node5.right = node7
    node6.left = node7
    
    print s.getSolution(node1, node4)
