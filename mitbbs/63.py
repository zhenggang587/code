
# The value of dp[i,j] is the cost of solving subproblem d[0 to i] while keeping the last element of the solution under s[j]. Note: this cost includes the cost of eliminating d[i] if it is less than s[j].

class Solution:
    def getSolution(self, A):
        if not A:
            return 0
        s = sorted(list(set(A)))

        m = len(A)
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            dp[0][j] = max(A[0] - s[j], 0)

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = (1 << 31)
                trim = A[i] - s[j]
                if trim < 0:
                    trim = A[i]

                for k in range(j + 1):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + trim)

        return min(dp[m - 1])


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([10, 1, 2, 3])
