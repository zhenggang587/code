
class ListNode:
    def __init__(self, x):
        self.val = x
        self.pre = None
        self.next = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity
        self.data = {}
        self.node_map = {}
        self.head = self.tail = ListNode(0)

    def addHits(self, key):
        if key not in self.node_map:
            self.node_map[key] = ListNode(key)

        node = self.node_map[key]
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre

        if self.tail == node:
            self.tail = node.pre
        if self.tail == self.head:
            self.tail = node

        node.next = self.head.next
        if self.head.next:
            self.head.next.pre = node
        self.head.next = node
        node.pre = self.head

    def evict(self):
        key = self.tail.val
        self.tail = self.tail.pre
        self.tail.next = None
        del self.data[key]
        del self.node_map[key]
        

    # @return an integer
    def get(self, key):
        if key not in self.data:
            return -1

        self.addHits(key)
        return self.data[key]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if not self.cap:
            return
        if len(self.data) == self.cap and key not in self.data:
            self.evict()

        self.data[key] = value
        self.addHits(key)



if __name__ == "__main__":
    l = LRUCache(1)
    l.get(2)
    l.set(2, 6)
    print l.get(1)
    l.set(1, 5)
    l.set(1, 2)
    print l.get(1)
    print l.get(2)
