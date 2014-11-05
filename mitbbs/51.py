import math

# missing two num
class Solution:
    def getSolution(self, A):
        n = len(A) + 2
        totalsum = n * (n + 1) / 2 - sum(A)
        squaresum = 0
        for a in A:
            squaresum += a * a
        squaresum = n * (n + 1) * (2 * n + 1) / 6 - squaresum

        sqrtsum = math.sqrt(2 * squaresum - totalsum * totalsum)
        return int((totalsum - sqrtsum) / 2), int((totalsum + sqrtsum) / 2)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([2, 3, 1])
