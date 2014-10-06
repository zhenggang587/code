
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head

        pre = dummy_node
        cur = head
        nex = cur.next
        while cur and nex:
            pre.next = nex
            temp = nex.next
            nex.next = cur
            cur.next = temp
            pre = cur
            cur = pre.next
            if not cur:
                break
            nex = cur.next


        return dummy_node.next

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
    #node1.next = node2
    #node2.next = node3
    node3.next = node4
    #node4.next = node5

    ret = s.swapPairs(node1)
    s.printList(ret)
