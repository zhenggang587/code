
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class MultiTreeNode:
    def __init__(self, x):
        self.val = x
        self.children = [None for i in range(4)]
        self.left = None
        self.right = None

class Solution:
    def getSolution(self, matrix):
        if not matrix:
            return []

        n = len(matrix)
        m = n * n
        row = col = 0
        ret = []
        for i in range(m):
            ret.append(matrix[row][col])
            if abs(row - col) % 2 == 0:
                row -= 1
                col += 1
                if row < 0 and col < n:
                    row = 0
                if col >= n:
                    row += 2
                    col -= 1
            else:
                row += 1
                col -= 1
                if col < 0 and row < n:
                    col = 0
                if row >= n:
                    col += 2
                    row -= 1
        return ret
                

if __name__ == "__main__":
    s = Solution()

    assert s.getSolution([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 16]]) == [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]
    assert s.getSolution([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
