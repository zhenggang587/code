
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0

        path = []
        return self.dfs(root, path)

    def dfs(self, node, path):
        path.append(node)

        ret = 0
        if node.left:
            ret += self.dfs(node.left, path)
        if node.right:
            ret += self.dfs(node.right, path)
        if not node.left and not node.right:
            sum = 0
            for pnode in path:
                sum = sum * 10 + pnode.val
            ret += sum
        path.remove(node)
        return ret
        

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    #node1.left = node2
    node1.right = node3

    print s.sumNumbers(node1)


