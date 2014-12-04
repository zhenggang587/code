
MAX_INT = (1 << 31)
class Solution:
    def getSolution(self, matrix, v):
        n = len(matrix)
        dist = [MAX_INT for i in range(n)]
        s = [False for i in range(n)]
        dist[v] = 0
        s[v] = True

        for i in range(n):
            if matrix[v][i] < MAX_INT:
                dist[i] = matrix[v][i]
        
        for i in range(1, n):
            u = i
            tmp = MAX_INT
            for j in range(n):
                if not s[j] and dist[j] < tmp:
                    tmp = dist[j]
                    u = j
            s[u] = True

            for j in range(n):
                if not s[j] and dist[u] + matrix[u][j] < dist[j]:
                    dist[j] = dist[u] + matrix[u][j]
        return dist


if __name__ == "__main__":
    s = Solution()

    print s.getSolution([[0, 2, 10],[0, 0, 3], [0, 0, 0]], 0)

