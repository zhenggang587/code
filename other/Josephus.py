
class Solution:
    def getSolution(self, A, m):
        f = 0
        for i in range(2, len(A) + 1):
            f = (f + m) % i
        return A[f]


if __name__ == "__main__":
    s = Solution()

    print s.getSolution([1, 2, 3, 4, 5], 3)
