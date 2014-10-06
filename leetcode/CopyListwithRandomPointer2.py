
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        cur = head
        while cur:
            new_cur = RandomListNode(cur.label)
            new_cur.next = cur.next
            cur.next = new_cur
            cur = new_cur.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        dummy = RandomListNode(0)
        p = dummy
        while cur:
            p.next = cur.next
            p = p.next
            cur.next = p.next
            cur = cur.next

        return dummy.next

    def printList(self, list):
        cur = list
        while cur:
            print cur.label, cur.random.label if cur.random else None
            cur = cur.next


if __name__ == "__main__":
    s = Solution()

    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    #node1.random = node4
    node2.random = node2
    node3.random = node1

    s.printList(s.copyRandomList(node1))
    s.printList(node1)
