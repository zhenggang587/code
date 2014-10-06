
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if not height:
            return 0

        stack = []
        stack.append((0, height[0]))
        left = [0 for h in height]
        for i in range(1, len(height)):
            while stack:
                index, h = stack[-1]
                if h < height[i]:
                    break
                stack.pop()
            if not stack:
                left[i] = i
            else:
                index, h = stack[-1]
                left[i] = i - index - 1
            stack.append((i, height[i]))

        stack = []
        stack.append((len(height) - 1, height[len(height) - 1]))
        right = [0 for h in height]
        for i in range(len(height) - 2, -1, -1):
            while stack:
                index, h = stack[-1]
                if h < height[i]:
                    break
                stack.pop()
            if not stack:
                right[i] = len(height) - 1 - i
            else:
                index, h = stack[-1]
                right[i] = index - 1 - i
            stack.append((i, height[i]))

        max_area = 0
        for i in range(len(height)):
            area = (left[i] + right[i] + 1) * height[i]
            if area > max_area:
                max_area = area

        return max_area
            
        
if __name__ == "__main__":
    s = Solution()

    assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
    assert s.largestRectangleArea([2, 2, 2, 2, 2]) == 10
    assert s.largestRectangleArea([4,2,0,3,2,4,3,4]) == 10
    assert s.largestRectangleArea([2, 2, 2, 2, 2]) == 10
