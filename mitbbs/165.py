
class Solution:
    def getSolution(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        hasVisited = set()
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and (i, j) not in hasVisited:
                    ret += 1
                    self.bfs(matrix, i, j, hasVisited)
        return ret

    def bfs(self, matrix, i, j, hasVisited):
        hasVisited.add((i, j))
        q = [(i, j)]
        while q:
            (i0, j0) = q.pop()
            for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                i, j = i0 + x, j0 + y
                if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                    continue
                if matrix[i][j] != 1 or (i, j) in hasVisited:
                    continue
                q.append((i, j))
                hasVisited.add((i, j))
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 0, 1],
                         [1, 0, 0],
                         [0, 1, 0]])
