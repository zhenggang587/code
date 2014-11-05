
# palindrome
# d[i][j] = d[i+1][j-1] if s[i]==s[j] else min(d[i+1][j], d[i][j-1] + 1) 
class Solution:
    def getSolution(self, s):
        n = len(s)
        d = [[0 for j in range(n+1)] for i in range(n+1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    d[i][j] = d[i + 1][j - 1]
                else:
                    d[i][j] = min(d[i + 1][j], d[i][j - 1]) + 1

        return d[0][n - 1]
            


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('a')
