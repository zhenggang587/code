
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getSolution(self, root):
        dummy = ListNode(0)
        dummy.next = root
        p = dummy
        q = root

        while q and q.next:
            p.next = q.next
            tmp = q.next.next
            q.next.next = q
            q.next = tmp
            p = q
            q = tmp
        return dummy.next

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
    s.printList(s.getSolution(node1))
