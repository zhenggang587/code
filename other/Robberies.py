
class Solution:
    def getSolution(self, A, limit):
        
        f[i][p] = f[i - 1][k] + A[0] if p - k >= A[1] else 0
if __name__ == "__main__":
    s = Solution()

