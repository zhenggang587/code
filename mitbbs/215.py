import random

maxHeight = 32
class SkipListNode:
    def __init__(self, val):
        self.val = val
        self.next = [None for i in range(maxHeight)]

class SkipList:
    def __init__(self):
        self.height = 0
        self.head = SkipListNode("")

    def set(self, val):
        level = 0
        while random.randint(0, 1) == 1:
            if level > self.height:
                self.height = level
                break
            level += 1

        node = SkipListNode(val)
        cur = self.head
        for i in range(self.height, -1, -1):
            while cur.next[i]:
                if cur.next[i].val > val:
                    break
                cur = cur.next[i]

            if i > level:
                continue
            node.next[i] = cur.next[i]
            cur.next[i] = node

    def draw(self):
        for i in range(self.height, -1, -1):
            cur = self.head
            while cur.next[i]:
                print i, cur.next[i].val
                cur = cur.next[i]
            print ''

if __name__ == "__main__":
    s = SkipList()

    s.set("a")
    s.set("b")
    s.set("c")
    s.set("d")
    s.set("e")
    s.set("f")
    s.set("g")
    s.set("h")
    
    s.draw()
