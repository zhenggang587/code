
# the problem may be min(max(|x-y|, |y-z|, |x-z|))
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getSolution(self, head1, head2, head3):
        p1, p2, p3 = head1, head2, head3
        ret = (1 << 31)
        while p1 and p2 and p3:
            d = max(abs(p1.val - p2.val), abs(p1.val - p3.val), abs(p2.val - p3.val))
            ret = min(ret, d)
            if p1.val < p2.val and p1.val < p3.val:
                p1 = p1.next
            elif p2.val < p1.val and p2.val < p3.val:
                p2 = p2.next
            else:
                p3 = p3.next
        return ret

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

    node6 = ListNode(2.5)
    node7 = ListNode(3.3)
    
    print s.getSolution(node1, node6, node7)
