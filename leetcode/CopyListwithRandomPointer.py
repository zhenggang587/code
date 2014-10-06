
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
            temp = cur.next
            new_cur = RandomListNode(cur.label)
            cur.next = new_cur
            new_cur.next = temp
            cur = temp

        old_cur = head
        new_cur = head.next
        while new_cur:
            if old_cur.random:
                new_cur.random = old_cur.random.next
            old_cur = new_cur.next
            if not old_cur:
                break
            new_cur = old_cur.next

        old_cur = head
        new_cur = new_head = head.next
        while new_cur:
            old_cur.next = new_cur.next
            old_cur = old_cur.next
            if not old_cur:
                break
            new_cur.next = old_cur.next
            new_cur = new_cur.next

        return new_head

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
    #node1.next = node2
    node2.next = node3
    node3.next = node4
    #node1.random = node4
    node2.random = node2
    node3.random = node1

    s.printList(s.copyRandomList(node1))
    s.printList(node1)
