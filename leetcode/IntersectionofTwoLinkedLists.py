
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pa = headA
        while pa.next:
            pa = pa.next
        pa.next = headB

        slow = fast = headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = headA
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                pa.next = None
                return fast
        pa.next = None
        return None

    
if __name__ == "__main__":
    s = Solution()

    a1 = ListNode('a1')
    a2 = ListNode('a2')
    a1.next = a2
    c1 = ListNode('c1')
    c2 = ListNode('c2')
    c3 = ListNode('c3')
    a2.next = c1
    c1.next = c2
    c2.next = c3

    b1 = ListNode('b1')
    b2 = ListNode('b2')
    b3 = ListNode('b3')
    b1.next = b2
    b2.next = b3
    b3.next = c1

    print s.getIntersectionNode(a1, b1).val
