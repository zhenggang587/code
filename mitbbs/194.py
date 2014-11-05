
'''
if rootA.color == "black":
    return A
if rootA.color == "white":
    return B
if rootA.color == "gray" and rootB.color == "gray".
##Pairwise intersect the subtrees of A and B.
##If all four of the returned subtrees have a black root, return a single node tree with a black root.
Otherwise return a tree with a gray root and the four returned subtrees as its subtrees.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getSolution(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1

        
    

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
