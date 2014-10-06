
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return None

        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = dummy_head
        fast = head
        while fast:
            cnt = 1
            while fast and fast.next:
                if fast.val == fast.next.val:
                    cnt += 1
                else:
                    break
                fast = fast.next
            if cnt == 1:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        slow.next = None
        return dummy_head.next

    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next
        

if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(2)
    node5 = ListNode(31)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    newnode = s.deleteDuplicates(node1)
    s.printList(newnode)
    
