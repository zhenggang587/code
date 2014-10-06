
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        size = len(A)
        left = 0
        right = len(A) - 1
        while left <= right:
            while left <= right and A[left] != elem:
                left += 1
            while right >= left and A[right] == elem:
                right -= 1
            if left < right:
                A[left] = A[right]
                left += 1
                right -= 1
        return right + 1

if __name__ == "__main__":
    s = Solution()

    assert s.removeElement([2], 2) == 0
    assert s.removeElement([2, 2, 2], 2) == 0
    assert s.removeElement([1, 1, 2], 2) == 2
    assert s.removeElement([1, 1, 1], 2) == 3
