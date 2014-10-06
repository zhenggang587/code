
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
        if not head:
            return None

        dummy_node = ListNode(0)
        dummy_node.next = head
        slow = head
        pre_slow = dummy_node
        while slow:
            if slow.val >= x:
                break
            pre_slow = slow
            slow = slow.next

        pre_fast = pre_slow
        fast = slow
        while fast:
            if fast.val < x:
                tmp = fast.next
                pre_fast.next = tmp

                pre_slow.next = fast
                fast.next = slow
                pre_slow = fast
                fast = tmp
            else:
                pre_fast = fast
                fast= fast.next

        return dummy_node.next

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
