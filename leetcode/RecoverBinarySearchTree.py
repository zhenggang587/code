
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if not root:
            return None

        found = [None, None]
        self.traverse(root, found)
        tmp = found[0].val
        found[0].val = found[1].val
        found[1].val = tmp
        return root

    def traverse(self, node, found):
        if not node.left and not node.right:
            return node, node
        
        min_left = max_left = node
        if node.left:
            min_left, max_left = self.traverse(node.left, found)
        min_right = max_right = node
        if node.right:
            min_right, max_right = self.traverse(node.right, found)

        if node.val < max_left.val:
            if not found[0] or found[0].val > node.val:
                found[0] = node
            if not found[1] or found[1].val < max_left.val:
                found[1] = max_left
        if node.val > min_right.val:
            if not found[0] or found[0].val > min_right.val:
                found[0] = min_right
            if not found[1] or found[1].val < node.val:
                found[1] = node
            
        return min_left, max_right

    def printTree(self, root):
        if not root:
            return
        print root.val
        self.printTree(root.left)
        self.printTree(root.right)

        
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(4)
    node1.left = node2
    node2.left = node3
    #node1.right = node3
    #node2.right = node4

    s.recoverTree(node1)
    s.printTree(node1)
