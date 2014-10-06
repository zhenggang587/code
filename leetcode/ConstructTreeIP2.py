
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        node = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        node.left = self.buildTree(inorder[:idx], postorder[:idx])
        node.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return node 
        

if __name__ == "__main__":
    s = Solution()

    node = s.buildTree([2, 3, 1, 4], [3, 2, 4, 1])

    print node.val
    print node.left.val
    print node.left.right.val
    print node.right.val
        
