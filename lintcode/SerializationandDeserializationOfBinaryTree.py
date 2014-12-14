
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.s = ''

    def serialize(self, root):
        self.s = ''
        self._serialize(root)
        return self.s

    def _serialize(self, root):
        if not root:
            self.s += '# '
            return
        
        self.s += str(root.val) + ' '
        self._serialize(root.left)
        self._serialize(root.right)

    def deserialize(self, data):
        self.s = data
        return self._deserialize()

    def _deserialize(self):
        i = 0
        while i < len(self.s) and self.s[i] != ' ':
            i += 1

        subs = self.s[:i]
        self.s = self.s[i + 1:]
        if not subs or subs == '#':
            return None

        root = TreeNode(int(subs))
        root.left = self._deserialize()
        root.right = self._deserialize()
        return root

if __name__ == "__main__":
    s = Solution()

    print s.serialize(s.deserialize('1 # # '))
