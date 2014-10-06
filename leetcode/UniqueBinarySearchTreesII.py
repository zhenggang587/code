
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        node_map = {}
        return self.traverse(1, n, node_map)

    def traverse(self, start, end, node_map):
        if start > end:
            return [None]
        if (start, end) in node_map:
            return node_map[(start, end)]
        if start == end:
            list = [TreeNode(start)]
            node_map[(start, end)] = list
            return list

        node_list = []
        for index in range(start, end + 1):
            left_list = self.traverse(start, index - 1, node_map)
            right_list = self.traverse(index + 1, end, node_map)
            for l in left_list:
                for r in right_list:
                    root = TreeNode(index)
                    root.left = l
                    root.right = r
                    node_list.append(root)
        node_map[(start, end)] = node_list
        return node_list
                    
    def printTree(self, root):
        if not root:
            return
        print root.val
        self.printTree(root.left)
        self.printTree(root.right)

        
if __name__ == "__main__":
    s = Solution()

    list = s.generateTrees(3)
    for l in list:
        s.printTree(l)
        print ''
