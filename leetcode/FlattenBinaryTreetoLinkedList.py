
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return

        stack = []
        stack.append(root)
        pre = TreeNode(-1)
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            pre.right = cur

            if cur.left:
                stack.append(cur.left)
            cur.left = None
            pre = cur
            
    def printList(self, list):
        cur = list
        pre = None
        while cur:
            print cur.val
            pre = cur
            cur = cur.right
        #print ''
        #while pre:
        #    print pre.val
        #    pre = pre.left

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.right = node6

    s.flatten(node1)
    s.printList(node1)
