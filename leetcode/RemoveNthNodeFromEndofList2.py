
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy_node = ListNode(0)
        dummy_node.next = head

        fast = head
        for i in range(n):
            fast = fast.next

        slow = dummy_node
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy_node.next

    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next
       
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
    
    ret = s.removeNthFromEnd(node1, 5)
    s.printList(ret)
