
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def removeNode(self, root, value):
        if not root:
            return None

        cur = root
        pre = None
        flag = 0
        while cur:
            if cur.val == value:
                break
            if cur.val > value:
                pre = cur
                cur = cur.left
                flag = 0
            else:
                pre = cur
                cur = cur.right
                flag = 1

        if not cur:
            return root

        if not cur.left and not cur.right:
            if not pre:
                return None
            if flag == 0:
                pre.left = None
            else:
                pre.right = None
            return root
        elif cur.left:
            tmpp = cur
            tmp = cur.left
            while tmp.right:
                tmpp = tmp
                tmp = tmp.right
            tmp.right = cur.right
            if tmpp != cur:
                tmpp.right = tmp.left
                tmp.left = cur.left
            if not pre:
                return tmp
            if flag == 0:
                pre.left = tmp
            else:
                pre.right = tmp
        else:
            tmpp = cur
            tmp = cur.right
            while tmp.left:
                tmpp = tmp
                tmp = tmp.left
            tmp.left = cur.left
            if tmpp != cur:
                tmpp.left = tmp.right
                tmp.right = cur.right
            if not pre:
                return tmp
            if flag == 0:
                pre.left = tmp
            else:
                pre.right = tmp

        return root
                

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(100)
    node3 = TreeNode(2)
    node4 = TreeNode(99)
    node5 = TreeNode(30)
    node6 = TreeNode(98)
    node7 = TreeNode(40)
    node8 = TreeNode(97)
    node1.right = node2
    node2.left = node3
    node3.right = node4
    node4.left = node5
    node5.right = node6
    node6.left = node7
    node7.right = node8

    root = s.removeNode(node1, 30)
    print node4.left.val
    print node4.left.right.left.val
