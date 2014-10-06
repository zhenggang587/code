
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if not numRows:
            return []

        row = [1 for i in range(numRows)]
        ret = []
        ret.append([1])
        for row_index in range(1, numRows):
            for col_index in range(row_index - 1, 0, -1):
                row[col_index] += row[col_index - 1] 
            ret.append(row[:row_index + 1])
        return ret
        

if __name__ == "__main__":
    s = Solution()

    print s.generate(1)
