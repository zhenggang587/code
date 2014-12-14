
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        left = 0
        right = len(num) - 1
        while left < right:
            if right - left == 1:
                return right if num[right] > num[left] else left
            mid = left + (right - left) / 2
            if mid == 0:
                return mid
            elif num[mid - 1] < num[mid]:
                left = mid
            else:
                right = mid - 1
        return left

        
if __name__ == "__main__":
    s = Solution()

    print s.findPeakElement([2])
    print s.findPeakElement([2, 3])
    print s.findPeakElement([3, 2])
    print s.findPeakElement([3, 2, 1])
    print s.findPeakElement([0, 1, 2, 1])
