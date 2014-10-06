
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        max_area = 0
        s = []
        i = 0
        while i < len(height):
            if not s or height[i] > height[s[-1]]:
                s.append(i)
                i += 1
            else:
                tmp = s.pop()
                if not s:
                    area = height[tmp] * i
                else:
                    area = height[tmp] * (i - s[-1] - 1)
                max_area = max(max_area, area)

        while s:
            tmp = s.pop()
            if not s:
                area = height[tmp] * len(height)
            else:
                area = height[tmp] * (len(height) - s[-1] - 1)
            max_area = max(max_area, area)

        return max_area
            
        
if __name__ == "__main__":
    s = Solution()

    assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
    assert s.largestRectangleArea([2, 2, 2, 2, 2]) == 10
    assert s.largestRectangleArea([4,2,0,3,2,4,3,4]) == 10
