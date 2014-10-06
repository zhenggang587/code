
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return True
            if A[mid] > A[left]:
                if target >= A[left] and target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[mid] < A[left]:
                if target > A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        
        return False
        
if __name__ == "__main__":
    s = Solution()

    assert s.search([2, 2, 2], -1) == False
    assert s.search([2, 2, 2], 2) == True
