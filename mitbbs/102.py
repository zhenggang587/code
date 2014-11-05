
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Iter:
    def __init__(self, root):
        self.p = root
        self.stack = []

    def hasNext(self):
        return self.stack or self.p

    def next(self):
        if not self.hasNext():
            raise Exception("no more")

        while self.stack or self.p:
            if self.p:
                self.stack.append(self.p)
                self.p = self.p.left
            else:
                self.p = self.stack.pop()
                tmp = self.p.val
                self.p = self.p.right
                return tmp

if __name__ == "__main__":
    
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3

    s = Iter(node1)
    while s.hasNext():
        print s.next()
