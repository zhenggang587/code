

class ListNode:
    def __init__(self, x):
        self.val = x
        self.pre = None
        self.next = None

class Solution:
    def __init__(self):
        self.head = ListNode(0)
        self.m = {}
        self.morethanone = set()

    def add(self, c):
        if c in self.morethanone:
            return

        if c in self.m:
            self.morethanone.add(c)
            node = self.m[c]
            node.pre.next = node.next
            node.next.pre = node.pre
            del self.m[c]
        else:
            node = ListNode(c)
            self.m[c] = node
            node.next = self.head.next
            if self.head.next:
                self.head.next.pre = node
            self.head.next = node
            node.pre = self.head
        
    def get(self):
        if self.head.next:
            return self.head.next.val
        return None

if __name__ == "__main__":
    s = Solution()
    
    s.add(1)
    s.add(2)
    print s.get()
    s.add(2)
    s.add(3)
    print s.get()
