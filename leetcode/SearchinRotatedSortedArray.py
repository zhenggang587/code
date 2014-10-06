
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            else:
                if A[mid] >= A[left]:
                    if target >= A[left] and target < A[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if target > A[mid] and target <= A[right]:
                        left = mid + 1
                    else:
                        right = mid - 1

        return -1
        

if __name__ == "__main__":
    s = Solution()

    assert s.search([3, 1], 1)==1
    assert s.search([3, 1], 3)==0
    assert s.search([3], 3)==0
    assert s.search([4, 5, 6, 7, 0, 1, 2], 4)==0
    assert s.search([4, 5, 6, 7, 0, 1, 2], 2)==6
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3)==-1
    assert s.search([4, 5, 6, 7, 0, 1, 2], -1)==-1
    assert s.search([4, 5, 6, 7, 0, 1, 2], 8)==-1
    assert s.search([4, 5, 6, 7, 0, 1, 2], 6)==2
    assert s.search([4, 5, 6, -1, 0, 1, 2], 1)==5

