
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):
        paths = []
        self.dfs(root, [], paths)
        return paths

    def dfs(self, node, path, paths):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            paths.append(path[:])
            path.pop()
            return

        self.dfs(node.left, path, paths)
        self.dfs(node.right, path, paths)
        path.pop()

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node1.right = node2
    node2.left = node3
    node2.right = node4
    
    print s.getSolution(node1)
