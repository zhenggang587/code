
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        l1_cur = l1
        l2_cur = l2

        dummy_root = ListNode(0)
        new_cur = dummy_root
        while l1_cur and l2_cur:
            if l1_cur.val < l2_cur.val:
                new_cur.next = l1_cur
                l1_cur = l1_cur.next
            else:
                new_cur.next = l2_cur
                l2_cur = l2_cur.next
            new_cur = new_cur.next
        if l1_cur:
            new_cur.next = l1_cur
        if l2_cur:
            new_cur.next = l2_cur

        return dummy_root.next

    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next

        
if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(0)
    node2 = ListNode(1)
    node1.next = node2

    node3 = ListNode(2)
    node4 = ListNode(4)
    node3.next = node4

    new_node = s.mergeTwoLists(node1, node3)
    s.printList(new_node)
