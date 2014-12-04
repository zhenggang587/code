
class Solution:
    def __init__(self):
        self.maxLen = 0
        self.maxStart = []
    
    def getSolution(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        d = [[1 for j in range(n + 1)] for i in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):    
                if i < m - 1 and abs(matrix[i+1][j] - matrix[i][j]) == 1:
                    d[i][j] = max(d[i][j], d[i+1][j] + 1)
                if j < n - 1 and abs(matrix[i][j+1] - matrix[i][j]) == 1: 
                    d[i][j] = max(d[i][j], d[i][j+1] + 1)
                if d[i][j] > self.maxLen:
                    self.maxLen = d[i][j]
                    self.maxStart = [(i, j)]
                elif d[i][j] == self.maxLen:
                    self.maxStart.append((i, j))

        paths = []
        for (i, j) in self.maxStart:
            self.traverse(matrix, d, i, j, [], paths)
        return paths     
                    
    def traverse(self, matrix, d, i, j, path, paths):
        path.append(matrix[i][j])
        if d[i][j] == 1:
            paths.append(path[:])
            return

        m = len(matrix)
        n = len(matrix[0])
        if i < m - 1 and d[i][j] == d[i+1][j] + 1:
            self.traverse(matrix, d, i+1, j, path, paths)
        if j < n - 1 and d[i][j] == d[i][j+1] + 1:
            self.traverse(matrix, d, i, j+1, path, paths)   
            
        path.pop() 
        

if __name__ == "__main__":
    s = Solution()

    print s.getSolution([[1, 3, 2, 6, 8], [-9, 7, 1, -1, 2], [1, 5, 0, 1, 9]])
