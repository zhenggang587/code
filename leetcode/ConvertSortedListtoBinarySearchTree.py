
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
        return self.convert(head)

    def convert(self, head):
        if not head:
            return None
        left, mid = self.findMid(head)
        if left == mid:
            return TreeNode(left.val)

        node = TreeNode(mid.val)
        node.left = self.convert(left)
        node.right = self.convert(mid.next)
        return node

    def findMid(self, head):
        slow = fast = head
        pre_slow = None
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        if pre_slow:
            pre_slow.next = None
        return  head, slow


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
