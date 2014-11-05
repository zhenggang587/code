import heapq

class Solution:
    def getSolution(self, matrix, k):
        if not matrix or not matrix[0]:
            return None

        m = len(matrix)
        n = len(matrix[0])
        i = j = 0
        p = 1
        hasVisited = set((i, j))
        h = [(matrix[i][j], i, j)]
        while p <= k and h:
            v, i, j = heapq.heappop(h)
            if p == k:
                return matrix[i][j]
            if i + 1 < m and (i + 1, j) not in hasVisited:
                heapq.heappush(h, (matrix[i + 1][j], i + 1, j))
                hasVisited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in hasVisited:
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))
                hasVisited.add((i, j + 1))
            p += 1

        return None
            

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 3, 5], [2, 4, 7]], 8)
