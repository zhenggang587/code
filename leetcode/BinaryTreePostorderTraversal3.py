
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
        ret = []
        cur = root
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right

                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    tmp.right = None
                    cur = cur.right

        return ret

     
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(3)
    node2 = TreeNode(1)
    node3 = TreeNode(2)
    node1.left = node2
    node1.right = node3

    print s.postorderTraversal(node1)

