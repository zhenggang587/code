
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        ret = ''
        for row in range(nRows):
            col = row
            while col < len(s):
                ret = ret + s[col]
                temp = col + 2 * (nRows - row - 1)
                if temp < len(s) and row != 0 and row != nRows - 1:
                    ret = ret + s[temp]
                col += 2 * (nRows - 1)

        return ret
        
if __name__ == "__main__":
    s = Solution()

    print s.convert('PAYPALISHIRING', 2)
