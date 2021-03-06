
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.s = ''

    def serialize(self, root):
        if not root:
            self.s += '# '
            return

        self.s += str(root.val) + ' '
        self.serialize(root.left)
        self.serialize(root.right)

    def deserialize(self):
        i = 0
        while i < len(self.s) and self.s[i] != ' ':
            i += 1
        subs = self.s[:i]
        self.s = self.s[i+1:]
        if not subs or subs == '#':
            return None
        node = TreeNode(int(subs))
        node.left = self.deserialize()
        node.right = self.deserialize()
        return node

if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode(10)
    node2 = TreeNode(2)
    node3 = TreeNode(35)
    node1.right = node2
    node2.left = node3
    s.serialize(node1)
    node = s.deserialize()
    print node.val
    print node.right.val
    print node.right.left.val
