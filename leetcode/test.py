
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'


class Solution:
    def getSolution(self, root):
    


if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(1) 
    node2 = ListNode(2) 
    node3 = ListNode(3) 
    node4 = ListNode(5) 
    node1.next = node2
    node2.next = node3

    s.printList(s.getSolution(node1))

