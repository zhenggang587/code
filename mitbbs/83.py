
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self, root):
        self.cur = root

    def hasNext(self):
        return self.cur != None

    def next(self):
        while self.cur:
            if not self.cur.left:
                ret = self.cur.val
                self.cur = self.cur.right
                return ret
            else:
                tmp = self.cur.left
                while tmp.right and tmp.right != self.cur:
                    tmp = tmp.right

                if not tmp.right:
                    tmp.right = self.cur
                    self.cur = self.cur.left
                else:
                    ret = self.cur.val
                    tmp.right = None
                    self.cur = self.cur.right
                    return ret

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3

    s = Solution(node1)
    while s.hasNext():
        print s.next()
    
