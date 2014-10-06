
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
        if not root:
            return []

        path = []
        path_sum = [0]
        paths = []
        self.dfs(root, path, path_sum, sum, paths)
        return paths

    def dfs(self, node, path, path_sum, sum, paths):
        path_sum[0] += node.val
        path.append(node.val)

        if not node.left and not node.right:
            temp = path_sum[0]
            if temp == sum:
                paths.append(path[::])
            path_sum[0] -= node.val
            path.pop()
            return

        if node.left:
            self.dfs(node.left, path, path_sum, sum, paths)
        if node.right:
            self.dfs(node.right, path, path_sum, sum, paths)

        path_sum[0] -= node.val
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
