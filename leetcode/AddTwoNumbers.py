
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0) 
        cur = dummy 
        s = 0
        while l1 or l2:
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            cur.next = ListNode(s % 10)
            cur = cur.next
            s /= 10
        if s:
            cur.next = ListNode(s)

        return dummy.next
        
    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next

if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    s.printList(s.addTwoNumbers(node1, node4))
