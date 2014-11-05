
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getSolution(self, head1, head2):
        m = set()
        p = head1
        while p:
            if p not in m:
                m.add(p)
            p = p.next

        q = head2
        while q:
            if q in m:
                return q
            q = q.next
        return None

if __name__ == "__main__":
    s = Solution()
    
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node5 = ListNode(5)
    node5.next = node2
    print s.getSolution(node1, node5).val
