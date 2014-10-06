
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        ret = []
        path = []
        for col in range(n):
            path.append(col)
            self.search(path, 1, n, ret)
            path.remove(col)
        return ret

    def search(self, path, row, n, ret):
        if row == n:
            one_res = []
            for pos in path:
                one_res.append('.' * pos + 'Q' + '.' * (n - 1 - pos))
            ret.append(one_res) 
            return
            
        for col in range(n):
            legal = True
            for pre_row in range(row):
                if not self.isLegal(pre_row, path[pre_row], row, col):
                    legal = False
                    break
            if legal:
                path.append(col)
                self.search(path, row + 1, n, ret)
                path.remove(col)

    def isLegal(self, row1, col1, row2, col2):
        if col1 == col2:
            return False
        k = (float(col2) - col1) / (row2 - row1)
        if k == 1.0 or k == -1.0:
            return False
        return True


if __name__ == "__main__":
    s = Solution()

    print s.solveNQueens(4)
