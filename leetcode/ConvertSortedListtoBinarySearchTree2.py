
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        return self.convert(head, 0, n - 1)

    def convert(self, head, start, end):
        if start > end:
            return None

        mid = start + (end - start) / 2
        left_node = self.convert(head, start, mid - 1)
        parent = TreeNode(head.val)
        parent.left = left_node
        head = head.next
        parent.right = self.convert(head, mid + 1, end)

        return parent


if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    treenode = s.sortedListToBST(node1)
    print treenode.val
    print treenode.left.val
    print treenode.left.left.val
    print treenode.right.val
