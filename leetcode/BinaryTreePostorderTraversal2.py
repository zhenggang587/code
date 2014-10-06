
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

        stack = [root]
        ret = []
        pre = None
        while stack:
            cur = stack[-1]
            if (not cur.left and not cur.right) or \
                (pre != None and (pre == cur.left or pre == cur.right)):
                stack.pop()
                ret.append(cur.val)
                pre = cur
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)

        return ret

     
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(3)
    node2 = TreeNode(1)
    node3 = TreeNode(2)
    node1.left = node2
    node1.right = node3

    print s.postorderTraversal(node1)

