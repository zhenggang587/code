
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        path = []
        paths = []
        self.dfs(root, 0, sum, path, paths)
        return paths

    def dfs(self, node, val, sum, path, paths):
        if not node:
            return
        val += node.val
        path.append(node.val)
        if not node.left and not node.right:
            if val == sum:
                paths.append(path[:])
            path.pop()
            return

        self.dfs(node.left, val, sum, path, paths)
        self.dfs(node.right, val, sum, path, paths)
        path.pop()
            
        
        
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
    node9 = TreeNode(5)
    node10 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node4.left = node7
    node4.right = node8
    node6.left = node9
    node6.right = node10

    print s.pathSum(node1, 22)
