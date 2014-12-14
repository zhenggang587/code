
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

INT_MAX = (1 << 31)

class Solution:
    def getSolution(self, A, B, pa, pb):
         

if __name__ == "__main__":
    s = Solution()

    print s.getSolution([[1, 2], [2, 5]], [[3, 4], [2, 8]], 1, 0)
