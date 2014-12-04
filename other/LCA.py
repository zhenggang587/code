class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
     
class Solution:
    def findDist(self, root, node1, node2):
        self.finished = False
        return self.LCA(root, node1, node2)

    def LCA(self, root, node1, node2):
        if not root:
            return 0

        d = 0
        if root == node1 or root == node2:
            d = 1

        l = self.LCA(root.left, node1, node2)
        r = self.LCA(root.right, node1, node2)
        if l * r or l * d or r * d:
            self.finished = True
            return l + r
        elif l or r or d:
            return l + r if self.finished else l + r + 1
        return 0

            
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1) 
    node2 = TreeNode(2) 
    node3 = TreeNode(3) 
    node4 = TreeNode(4) 
    node5 = TreeNode(5) 

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    assert s.findDist(node1, node4, node1) == 2
    assert s.findDist(node1, node4, node5) == 2
    assert s.findDist(node1, node4, node3) == 3

