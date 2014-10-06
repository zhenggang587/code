import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if not list:
            return None

        node_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(node_heap, (lists[i].val, lists[i]))

        dummy = cur = ListNode(-1)
        while node_heap:
            val, node = heapq.heappop(node_heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(node_heap, (node.next.val, node.next))

        return dummy.next
        

    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next


if __name__ == "__main__":
    s = Solution()
    node3 = ListNode(10)
    node2 = ListNode(5)
    node2.next = node3
    node1 = ListNode(8)
    node0 = ListNode(2)
    node0.next = node1
    node4 = None

    list = [node0, node2, node4]
    s.printList(s.mergeKLists(list))
