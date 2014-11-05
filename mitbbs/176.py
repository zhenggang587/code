
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root, key):
        if not root:
            return None

        minVal = abs(root.val - key)
        minNode = root
        cur = root
        while cur:
            if abs(cur.val - key) < minVal:
                minVal = abs(cur.val - key)
                minNode = cur

            if cur.val == key:
                return cur
            elif cur.val < key:
                cur = cur.right
            else:
                cur = cur.left
        return minNode
            

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
