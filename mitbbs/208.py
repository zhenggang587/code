class ListNode:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None
        

class Solution:
    def __init__(self, capacity):
        self.cap = capacity
        self.head = self.tail = ListNode(0)
        self.m = {}
        self.data = {}

    def get(self, key):
        if key not in self.data:
            return None

        self._hit(key)
        return self.data[key]

    def set(self, key, val):
        if key not in self.data and len(self.data) == self.cap:
            self._evict()

        self._hit(key)
        self.data[key] = val

    def _hit(self, key):
        if key not in self.m:
            self.m[key] = ListNode(key)

        node = self.m[key]
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre

        if node == self.tail:
            self.tail = node.pre
        if self.tail == self.head:
            self.tail = node

        node.next = self.head.next
        if self.head.next:
            self.head.next.pre = node
        self.head.next = node
        node.pre = self.head

    def _evict(self):
        if not self.cap:
            return

        key = self.tail.val
        self.tail = self.tail.pre
        self.tail.next = None
        del self.m[key]
        del self.data[key]
        

if __name__ == "__main__":
    s = Solution(1)
    
    s.set(2, 1)
    print s.get(2)
    s.set(3, 2)
    print s.get(2)
    print s.get(3)
