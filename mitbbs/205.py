
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):
        if not root:
            return '', '', ''
        if root.left.val not in '+-*/' and root.right.val not in '+-*/':
            return root.val, root.left.val, root.right.val

        lval, ll, lr = self.getSolution(root.left)
        rval, rl, rr = self.getSolution(root.right)
        if root.left.val not in '+-*/':
            l = root.left.val
        else:
            l = ll + root.left.val + lr
            if root.left.val in '+-' and root.val in '*/':
                l = '(' + l + ')'

        if root.right.val not in '+-*/':
            r = root.right.val
        else:
            r = rl + root.right.val + rr
            if (root.right.val in '+-' and root.val in '*/') or \
                (root.right.val in '-' and root.val in '-') or \
                (root.right.val in '/' and root.val in '/'):
                r = '(' + r + ')'

        return root.val, l, r

    def GetSolution(self, root):
        v, l, r = self.getSolution(root)
        return l + v + r
        

if __name__ == "__main__":
    s = Solution()

    node1 = TreeNode('*')
    node2 = TreeNode('*')
    node3 = TreeNode('*')
    node1.left = node2
    node1.right = node3

    node4 = TreeNode('1')
    node5 = TreeNode('2')
    node2.left = node4
    node2.right = node5

    node6 = TreeNode('4')
    node7 = TreeNode('5')
    node3.left = node6
    node3.right = node7

    
    print s.GetSolution(node1)
