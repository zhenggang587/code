
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        row_length = len(matrix)
        col_length = len(matrix[0])
        s = [[0 for j in range(col_length)] for i in range(row_length)]

        for j in range(col_length):
            if matrix[0][j] == '1':
                s[0][j] = 1
            for i in range(1, row_length):
                if matrix[i][j] == '1': 
                    s[i][j] = s[i - 1][j] + 1

        max_area = 0
        for j in range(row_length):
            h = self.maxHeight(s[j])
            if h > max_area:
                max_area = h

        return max_area

    def maxHeight(self, height):
        if not height:
            return 0

        left = [0 for h in height]
        stack = []
        stack.append((0, height[0]))
        for i in range(1, len(height)):
            while stack:
                index, h = stack[-1]
                if height[i] > h:
                    break
                stack.pop()
            if not stack:
                left[i] = i
            else:
                index, h = stack[-1]
                left[i] = i - index - 1
            stack.append((i, height[i]))
                
        right = [0 for h in height]
        stack = []
        stack.append((len(height) - 1, height[len(height) - 1]))
        for i in range(len(height) - 2, -1, -1):
            while stack:
                index, h = stack[-1]
                if height[i] > h:
                    break
                stack.pop()
            if not stack:
                right[i] = len(height) - 1 - i
            else:
                index, h = stack[-1]
                right[i] = index - i - 1
            stack.append((i, height[i]))

        max_height = 0
        for i in range(len(height)):
            if (left[i] + right[i] + 1) * height[i] > max_height:
                max_height = (left[i] + right[i] + 1) * height[i]
        return max_height
        
if __name__ == "__main__":
    s = Solution()

    print s.maximalRectangle(
    ['111', '001']
    )
