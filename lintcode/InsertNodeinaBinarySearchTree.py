
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node

        cur = root
        pre = None
        while cur:
            pre = cur
            if cur.val > node.val:
                cur = cur.left
            else:
                cur = cur.right

        if pre.val > node.val:
            pre.left = node
        else:
            pre.right = node
        return root
                

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node3 = TreeNode(4)
    node4 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node3.left = node4

    node = TreeNode(6)
    root = s.insertNode(node1, node)
    print root.right.right.val
