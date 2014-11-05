
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getSolution(self, head1, head2):
        p2 = head2
        m2 = {}
        while p2:
            if p2.val not in m2:
                m2[p2.val] = 0
            else:
                break
            p2 = p2.next

        p1 = head1
        m1 = {}
        ret = set()
        while p1:
            if p1 not in m1:
                m1[p1] = 0
                if p1.val not in m2:
                    ret.add(p1.val)
            else:
                break
            p1 = p1.next
        return ret
        

if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2

    node3 = ListNode(2)
    
    print s.getSolution(node1, node3)
