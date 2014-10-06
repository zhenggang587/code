
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy_node = ListNode(0)
        dummy_node.next = head

        index = 1
        h = dummy_node
        while index < m:
            h = h.next
            index += 1

        pre, cur = h.next, h.next.next
        while index < n:
            pre.next = cur.next
            cur.next = h.next
            h.next = cur
            cur = pre.next 
            index += 1

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

    s.printList(s.reverseBetween(node1, 2, 4))
