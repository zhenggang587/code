import threading

# 改进用hashmap+双向链表快速删除

class observer:
    def __init__(self, val):
        self.val = val

    def updated(self):
        print 'notify ', self.val 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class foo:
    def __init__(self):
        self.head = ListNode(None)
        self.val = None
        self.lock = threading.Lock()
        
    def register(self, ob):
        with self.lock:
            next = self.head.next
            cur = ListNode(ob)
            self.head.next = cur
            cur.next = next

    def unregister(self, ob):
        with self.lock:
            cur = self.head
            while cur.next:
                if cur.next.val == ob:
                    cur.next = cur.next.next
                    return
                cur = cur.next

    def changeValue(self, newvalue):
        with self.lock:
            self.val = newvalue

            cur = self.head
            while cur.next:
                cur.next.val.updated()
                cur = cur.next

if __name__ == "__main__":
    f = foo()
    ob1 = observer(1)
    ob2 = observer(2)
    f.register(ob1)
    f.changeValue('a')
    f.register(ob2)
    f.changeValue('b')
    f.unregister(ob1)
    f.changeValue('c')
