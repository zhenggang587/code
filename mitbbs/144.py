
class Solution:
    def getSolution(self, n):
        u = [(3000, 0.15), (5000, 0.25), (10000, 0.5)]
        ret = 0.0
        for i in range(len(u)):
            if n < u[i][0]:
                break
            if i + 1 < len(u):
                ret += (u[i + 1][0] - u[i][0]) * u[i][1]
            else:
                ret += (n - u[i][0]) * u[i][1]
                break
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(15000)
