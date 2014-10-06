
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

        i = 0
        while i < n:
            fast = fast.next
            i += 1

        pre_slow = dummy_node
        slow = head
        while fast:
            fast = fast.next
            pre_slow = slow
            slow = slow.next
        pre_slow.next = slow.next
        del slow

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
