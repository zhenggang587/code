
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        left = ListNode(0)
        right = ListNode(0)
        p = left
        q = right
        cur = head
        while cur:
            if cur.val < x:
                p.next = cur
                p = p.next
            else:
                q.next = cur
                q = q.next
            cur = cur.next
        p.next = right.next
        q.next = None

        return left.next

    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next
        
if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(2)
    node2 = ListNode(1)
    node1.next = node2

    ret = s.partition(node1, 2)
    s.printList(ret)
