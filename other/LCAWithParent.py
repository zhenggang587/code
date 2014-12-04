
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.parent = None
     
class Solution:
    def LCA(self, node1, node2):
        path1 = []
        p1 = node1
        while p1:
            path1.insert(0, p1)
            p1 = p1.parent

        path2 = []
        p2 = node2
        while p2:
            path2.insert(0, p2)
            p2 = p2.parent

        i, j = 0, 0
        ret = None
        while i < len(path1) and j < len(path2) and path1[i] == path2[j]:
            ret = path1[i]
            i += 1
            j += 1
        return ret
            
            
if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode(1) 
    node2 = TreeNode(2) 
    node3 = TreeNode(3) 
    node4 = TreeNode(4) 
    node5 = TreeNode(5) 

    node1.left = node2
    node2.parent = node1
    node1.right = node3
    node3.parent = node1
    node2.left = node4
    node4.parent = node2
    node2.right = node5
    node5.parent = node2

    print s.LCA(node4, node5).val
