
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not k or not head:
            return head
        slow = fast = head

        for i in range(k):
            if not fast.next:
                fast = head
            else:
                fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head;
        newhead = slow.next
        slow.next = None
        return newhead

    def printList(self, node):
        while node:
            print node.val
            node = node.next
        
if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1 = s.rotateRight(node1, 5)
    s.printList(node1)
