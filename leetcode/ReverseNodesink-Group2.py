
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        i = 0
        pre, cur = dummy, head
        while cur:
            i += 1
            if i % k == 0:
                pre = self.reverse(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next

        return dummy.next

    def reverse(self, pre, p):
        last = pre.next
        cur = last.next
        while cur != p:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next

        return last

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
    node6 = ListNode(6)
    node7 = ListNode(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    ret = s.reverseKGroup(node1, 2)
    s.printList(ret)
