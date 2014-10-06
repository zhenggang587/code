
class Solution:
    # @return an integer
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            min_height = min(height[left], height[right])
            if min_height * (right - left) > max_area:
                max_area = min_height * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        
if __name__ == "__main__":
    s = Solution()

    print s.maxArea([4, 7, 5, 7, 6])
