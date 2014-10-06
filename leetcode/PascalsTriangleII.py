
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        numRows = rowIndex + 1

        row = [1 for i in range(numRows)]
        for row_index in range(1, numRows):
            for col_index in range(row_index - 1, 0, -1):
                row[col_index] += row[col_index - 1] 
        return row


if __name__ == "__main__":
    s = Solution()

    print s.getRow(0)

