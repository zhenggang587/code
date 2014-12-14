
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num:
            return -1

        left = 0
        right = len(num) - 1
        while left < right:
            mid = left + (right - left) / 2
            if num[mid] < num[right]:
                right = mid
            else:
                left = mid + 1
        return num[right]

if __name__ == "__main__":
    s = Solution()

    print s.findMin([1, 2])
