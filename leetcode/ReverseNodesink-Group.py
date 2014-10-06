
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        list_len = 0
        node = head
        while node:
            list_len += 1
            node = node.next
        if list_len < k:
            return head

        dummy_node = ListNode(0)
        dummy_node.next = head

        pre = head
        cur = pre.next
        left_len = list_len
        pre_k = dummy_node
        while cur and left_len >= k:
            i = 1
            cur_k = pre_k.next 
            while cur and i < k:
                tmp = cur.next if cur else None
                cur.next = pre
                pre = cur
                cur = tmp
                i += 1
            pre_k.next = pre
            pre_k = cur_k

            cur_k.next = cur
            pre = cur
            cur = pre.next if pre else None
            
            left_len -= k

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
    node6 = ListNode(6)
    node7 = ListNode(7)
    node1.next = node2
    #node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    ret = s.reverseKGroup(node1, 1)
    s.printList(ret)
