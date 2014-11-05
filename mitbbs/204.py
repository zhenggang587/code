#!/env/python
#encoding:utf8

import sys 
import json

reload(sys)
sys.setdefaultencoding("utf-8")

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root):
        cur = [root]
        next = []
        sub1 = []
        sub2 = []
        depth = self.getDepth(root)
        level = 1
        while cur:
            for i in range(len(cur)):
                node = cur[i]
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            sub1.append(cur[0].val)
            if len(cur) != 1:
                sub2.append(cur[len(cur) - 1].val)

            if level == depth - 1:
                for i in range(len(cur)):
                    node = cur[i]
                    if node.left and node.right:
                        sub1.append(node.left.val)
                        sub1.append(node.right.val)
                    else:
                        if node.left:
                            sub1.append(node.left.val)
                        if i > 0 and i < len(cur) - 1:
                            sub1.append(node.val)
                        if node.right:
                            sub1.append(node.right.val)
                break
                
            level += 1
            cur = next
            next = []
        sub1.extend(sub2[::-1])
        return sub1

    def getDepth(self, root):
        if not root:
            return 0

        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

if __name__ == "__main__":
    s = Solution()
    
    node1 = TreeNode('苹果')
    node2 = TreeNode('梨')
    node3 = TreeNode('番茄')
    node1.left = node2
    node1.right = node3

    node4 = TreeNode('桃子')
    node5 = TreeNode('李子')
    node2.left = node4
    node2.right = node5

    node6 = TreeNode('茄子')
    node7 = TreeNode('筷子')
    node3.left = node6
    node3.right = node7

    node8 = TreeNode('勺子')
    node9 = TreeNode('镜子')
    node4.left = node8
    node4.right = node9

    node10 = TreeNode('盘子')
    node11 = TreeNode('刀子')
    node5.left = node10
    node5.right = node11

    node12 = TreeNode('傻子')
    node6.left = node12

    print s.getSolution(node1)
