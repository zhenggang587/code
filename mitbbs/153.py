
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, root, key, m):
        s = self.findClosest(root, key)
        node = s.pop()
        ret.append(node)
        m -= 1

        leftS = s[:]
        rightS = s[:]
        smallerNode = self.findLeftLargest(leftS, node)
        largerNode = self.findLeftLargest(rightS, node)
        while m > 0:
            if not smallerNode and not largerNode:
                break
            if smallerNode and largerNode:
                if abs(smallerNode.val - key) < abs(largerNode.val - key):
                    ret.append(smallerNode)
                    smallerNode = self.findLeftLargest(smallerNode, leftS)
                else:
                    ret.append(largerNode)
                    largerNode = self.findRightSmallest(largerNode, rightS)
            elif smallerNode:
                ret.append(smallerNode)
                smallerNode = self.findLeftLargest(smallerNode, leftS)
            else:
                ret.append(largerNode)
                largerNode = self.findRightSmallest(largerNode, rightS)
            m -= 1
        return ret


    def findClosest(self, root, key):
        s = []
        cur = root
        closestNode = None
        closestDist = (1 << 31)
        while cur:
            s.append(cur)
            if abs(cur.val - key) < closestDist:
                closestNode = cur
                closestDist = abs(cur.val - key)

            if cur.val == key:
                return s
            elif cur.val > key:
                cur = cur.left
            else:
                cur = cur.right

        return s

    def findLeftLargest(self, s, node):
        if node.left:
            cur = node.left
            while cur.right:
                s.append(cur)
                cur = cur.right
            return cur
        else:
            while s:
                cur = s.pop()
                if cur.val < node.val:
                    return cur
            return None

    def findRightSmallest(self, s, node):
        if node.right:
            cur = node.right
            while cur.left:
                s.append(cur)
                cur = cur.left
            return cur
        else:
            while s:
                cur = s.pop()
                if cur.val > node.val:
                    return cur
            return None
                

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(None, 1, 1)
