
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        cur = 0
        last = 1
        ret = []
        while queue:
            tmp = last
            row = []
            while cur < last:
                node = queue.pop(0)
                row.append(node.val)
                cur += 1
                if node.left:
                    queue.append(node.left)
                    tmp += 1
                if node.right:
                    queue.append(node.right)
                    tmp += 1
            ret.append(row)
            cur = last
            last = tmp
        return ret
        
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    print s.levelOrder(node1)
