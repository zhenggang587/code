
class Solution:
    def getSolution(self, A, target):
        total = sum(A)
        start = 0
        end = len(A) - 1
        while start <= end:
            if total <= target:
                return end - start + 1
            if A[start] < A[end]:
                total -= A[end]
                end -= 1
            else:
                total -= A[start]
                start += 1
        return 0

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 1, 2, 1, 1], 5)
    print s.getSolution([10,1,1,1,1,3,6,7], 8)
    print s.getSolution([1, -2, 4, 5, -2, 6, 7], 7)
