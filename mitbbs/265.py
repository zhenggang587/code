
# see 108.py

class Solution:
    def getSolution(self, matrix, word):
        if not matrix or not matrix[0] or not word:
            return None

        m = len(matrix)
        n = len(matrix[0])

        paths = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == word[0]:
                    path = [(i, j)]
                    self.traverse(matrix, i, j, word, 1, path, paths)

        return paths

    def traverse(self, matrix, row, col, word, index, path, paths):
        if index == len(word):
            paths.append(path[:])
            return

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue

                rowi, colj = row + i, col + j
                if rowi < 0 or rowi >= len(matrix) or colj >= len(matrix[0]) or colj < 0:
                    continue
                if matrix[rowi][colj] != word[index] or (rowi, colj) in path:
                    continue
                path.append((rowi, colj))
                self.traverse(matrix, rowi, colj, word, index + 1, path, paths)
                path.pop()
        

if __name__ == "__main__":
    s = Solution()

    print s.getSolution([['e', 'g', 'o', 'd'], 
                         ['a', 'c', 'a', 't'], 
                         ['e', 'a', 't', 'e'], 
                         ['k', 't', 'q', 'z']], 'cat')
