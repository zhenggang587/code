
class Solution:
    def getSolution(self, A, k):
        hasVisited = set()
        n = len(A)
        total = self.combine(n, k)
        groups = []
        for i in range(n):
            if i in hasVisited:
                continue
            j = i
            cycle = set()
            while j not in cycle:
                hasVisited.add(j)
                cycle.add(j)
                j = A[j] - 1
            groups.append(len(cycle))
        
        m = len(groups)
        if k < m:
            return 0.0
        f = [[1 if j == 0 else 0 for j in range(k + 1)] for i in range(m + 1)]
        same = 0
        for i in range(m):
            for j in range(k + 1):
                for l in range(1, j + 1):
                    f[i + 1][j] += self.combine(groups[i], l) * f[i][j - l]
        return f[m][k] / total
        
    def combine(self, n, k):
        total = 1.0
        div = 1.0
        for i in range(k):
            total *= (n - i)
            div *= (i + 1)
        return total / div
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([2, 5, 4, 3, 1], 1)
    print s.getSolution([2, 5, 4, 3, 1], 2)
    print s.getSolution([2, 5, 4, 3, 1], 3)
    print s.getSolution([2, 5, 4, 3, 1], 4)
