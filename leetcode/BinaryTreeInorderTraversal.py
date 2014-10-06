
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return []

        stack = []
        stack.append(root)
        ret = []
        has_visited = set()
        has_visited.add(root)
        while stack:
            node = stack[-1]
            while node.left and node.left not in has_visited:
                stack.append(node.left)
                node = node.left
                has_visited.add(node)
            if not node.right or node.right not in has_visited:
                ret.append(node.val)

            if node.right and node.right not in has_visited:
                stack.append(node.right)
                has_visited.add(node.right)
            else:
                stack.pop()
        return ret
        
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    #node1.right = node2
    node2.left = node3

    print s.inorderTraversal(node1)

