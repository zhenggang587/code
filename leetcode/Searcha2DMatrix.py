
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        left_row = 0
        right_row = len(matrix) - 1
        while left_row <= right_row:
            middle_row = left_row + (right_row - left_row) / 2
            if len(matrix[middle_row]) <= 0:
                return False
            if matrix[middle_row][0] == target:
                return True
            elif matrix[middle_row][0] > target:
                right_row = middle_row - 1
            elif matrix[middle_row][len(matrix[middle_row]) - 1] < target:
                left_row = middle_row + 1
            else:
                return self.searchRow(matrix[middle_row], target)
        return False

    def searchRow(self, row, target):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False



if __name__ == "__main__":
    s = Solution()

    print s.searchMatrix([
], -1)
