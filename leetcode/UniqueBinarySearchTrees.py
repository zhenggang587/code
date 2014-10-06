
class Solution:
    # @return an integer
    def numTrees(self, n):
        if n <= 1:
            return 1
        f = [0 for i in range(n + 1)]
        f[0] = f[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                f[i] += f[j - 1] * f[i - j]

        return f[n]

        
if __name__ == "__main__":
    s = Solution()

    print s.numTrees(2)
