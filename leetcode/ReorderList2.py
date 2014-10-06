
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return

        mid = self.findMid(head)
        mid = self.reverse(mid)

        left_cur = head
        right_cur = mid
        while left_cur.next:
            temp_left = left_cur.next
            left_cur.next = right_cur
            
            right_cur = right_cur.next
            left_cur.next.next = temp_left

            left_cur = temp_left

        left_cur.next = right_cur

        return head
            

    def findMid(self, head):
        slow, fast, pre_slow = head, head, None
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        pre_slow.next = None
        return slow

    def reverse(self, head):
        dummy = ListNode(0) 
        cur = head
        while cur:
            tmp = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = tmp
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

    s.printList(s.reorderList(node1))
