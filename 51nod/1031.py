
class Solution:
    def getSolution(self, n):
        if n == 0:
            return 0
        f = [1 for i in range(n + 1)]

        for i in range(2, n + 1):
            f[i] =  f[i - 2] + f[i - 1]
        return f[n]

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(3)
