
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        pre_mid, mid = self.findMid(head)
        mid = self.reverse(mid)

        left_cur = head
        right_cur = mid
        while left_cur and right_cur:
            temp_left = left_cur.next
            left_cur.next = right_cur
            
            temp_right = right_cur.next
            right_cur.next = temp_left

            left_cur = temp_left
            right_cur = temp_right

        return head
            

    def findMid(self, head):
        if not head:
            return None, None
        slow = fast = head
        pre_slow = None
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        if slow.next: # left len is equal or greater than right
            pre_slow = slow
            slow = slow.next
        if pre_slow:
            pre_slow.next = None
        return pre_slow, slow

    def reverse(self, head):
        if not head:
            return None
        pre = head
        cur = head.next
        while cur:
            ne = cur.next
            cur.next = pre
            pre = cur
            cur = ne
        head.next = None
        return pre
            
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
    #node3.next = node4
    node4.next = node5

    s.printList(s.reorderList(node1))
