
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root:
            return []

        stack = []
        ret = []
        hasVisited = set()
        hasVisited.add(None)
        stack.append(root)
        while stack:
            node = stack[-1]

            if node.right and node.right not in hasVisited:
                stack.append(node.right)
            if node.left and node.left not in hasVisited:
                stack.append(node.left) 
            if not node.left and not node.right \
            or (node.left in hasVisited and node.right in hasVisited):
                ret.append(node.val)
                hasVisited.add(node)
                stack.pop()

        return ret

     
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(3)
    node2 = TreeNode(1)
    node3 = TreeNode(2)
    node1.left = node2
    node1.right = node3

    print s.postorderTraversal(node1)

