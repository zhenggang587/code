
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getSolution(self, num):
        if num == 0:
            return ListNode(0)

        signed = False
        if num < 0:
            signed = True
            num = -num

        p = dummy = ListNode(-1)
        while num:
            q = ListNode(num % 10)
            q.next = p.next
            p.next = q
            num /= 10

        if signed:
            q = ListNode('-')
            q.next = p.next
            p.next = q

        return dummy.next

    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next


if __name__ == "__main__":
    s = Solution()
    
    s.printList(s.getSolution(-123))
