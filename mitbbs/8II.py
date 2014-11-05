
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.stack = []

    def getSolution(self, root, key, m):
        if m == 0 or not root:
            return None

        ret = []
        self.findNearest(root, key)
        node = self.stack.pop()
        ret.append(node)
        m -= 1

        self.largerStack = self.stack[:]
        self.smallerStack = self.stack[:]
        smallerNode = self.findSmaller(node)
        largerNode = self.findLarger(node)
        while m > 0:
            if not smallerNode and not largerNode:
                break
            if smallerNode and largerNode:
                if abs(smallerNode.val - key) < abs(largerNode.val - key):
                    ret.append(smallerNode)
                    smallerNode = self.findSmaller(smallerNode)
                else:
                    ret.append(largerNode)
                    largerNode = self.findLarger(largerNode)
            elif smallerNode:
                ret.append(smallerNode)
                smallerNode = self.findSmaller(smallerNode)
            else:
                ret.append(largerNode)
                largerNode = self.findLarger(largerNode)
            m -= 1
        return ret

    def findSmaller(self, node):
        if node.left:
            cur = node.left
            while cur.right:
                self.smallerStack.append(cur)
                cur = cur.right
            return cur
        else:
            while self.smallerStack:
                cur = self.smallerStack.pop()
                if cur.val < node.val:
                    return cur
            return None

    def findLarger(self, node):
        if node.right:
            cur = node.right
            while cur.left:
                self.largerStack.append(cur)
                cur = cur.left
            return cur
        else:
            while self.largerStack:
                cur = self.largerStack.pop()
                if cur.val > node.val:
                    return cur
            return None

    def findNearest(self, root, key):
        minVal = abs(root.val - key)
        minNode = root
        cur = root
        while cur:
            self.stack.append(cur)
            dist = abs(cur.val - key)
            if dist < minVal:
                minVal = dist
                minNode = cur

            if dist == 0:
                return
            elif cur.val > key:
                cur = cur.left
            else:
                cur = cur.right
        

    def printNode(self, node):
        for i in node:
            print i.val

if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node1.left = node3
    node3.right = node2

    node4 = TreeNode(4)
    node1.right = node4
    ret = s.getSolution(node1, 3, 3)
    s.printNode(ret)
