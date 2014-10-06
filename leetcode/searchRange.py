
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left_pos = self.searchLeft(A, target)
        right_pos = self.searchRight(A, target)
        return [left_pos, right_pos]

    def searchLeft(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left < len(A) and A[left] == target:
            return left
        return -1

    def searchRight(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0 and A[right] == target:
            return right
        return -1



if __name__ == "__main__":
    s = Solution()

    print s.searchRange([5, 7, 7, 8, 8, 10], 1)
