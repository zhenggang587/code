

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return None

        dummy_node = ListNode(0)
        dummy_node.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = dummy_node
                while pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                cur = cur.next
            
        return dummy_node.next
            
    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next


if __name__ == "__main__":
    s = Solution()
    node3 = ListNode(1)
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(3)
    node1.next = node2

    s.printList(s.insertionSortList(node1))
