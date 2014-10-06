
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return None

        slow = head
        fast = head.next
        while fast:
            if slow.val != fast.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        slow.next = None
        return head

    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next
        

if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s.deleteDuplicates(node1)
    s.printList(node1)
