
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse(self, s):
        if not s:
            return [None]
        
        ret = []
        for i in range(1, len(s) + 1):
            lt = self.traverse(s[1:i])
            rt = self.traverse(s[i:])
            for l in lt:
                for r in rt:
                    root = TreeNode(s[0])
                    root.left = l
                    root.right = r
                    ret.append(root)
        return ret
                    


if __name__ == "__main__":
    s = Solution()
    
    ret = s.traverse('123')
    print len(ret)
