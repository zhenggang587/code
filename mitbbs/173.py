import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getSolution(self, root):
        node = root
        cur = root
        n = 1
        while cur:
            k = random.randint(1, n)
            if k == n:
                node = cur
            cur = cur.next
            n += 1
        return node

if __name__ == "__main__":
    s = Solution()
    
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    m = {1: 0, 2: 0, 3: 0}
    for i in range(10000):
        m[s.getSolution(node1).val] += 1
    print m
