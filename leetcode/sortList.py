
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        (left_head, right_head) = self.findMid(head)
        if left_head != right_head:
            left_list = self.sortList(left_head)
            right_list = self.sortList(right_head)
            return self.mergeList(left_list, right_list)
        else:
            return left_head
        
    def findMid(self, head):
        slow = fast = head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if prev_slow:
            prev_slow.next = None
        return head, slow

    def mergeList(self, left_head, right_head):
        left_p = left_head
        right_p = right_head
        cur = new_head = ListNode(-1)
        while left_p and right_p:
            if left_p.val < right_p.val:
                cur.next = left_p
                left_p = left_p.next
            else:
                cur.next = right_p
                right_p = right_p.next
            cur = cur.next
        if left_p:
            cur.next = left_p
        elif right_p:
            cur.next = right_p
        return new_head.next


    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next

if __name__ == "__main__":
    s = Solution()
    node1 = None

    s.printList(s.sortList(node1))
