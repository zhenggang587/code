
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):
        if not root:
            return None

        queue = [root]
        ret = []
        while queue:
            n = len(queue)
            for k in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if k == n - 1:
                    ret.append(node.val)
        return ret
                

if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node1.left = node2
    node2.left = node3

    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.right = node4
    #node4.right = node5
    print s.getSolution(node1)
