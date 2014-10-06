
class Solution:
    def getSolution(self, A):
        s = 0
        for a in A:
            s += a
        d = [0 for i in range(s + 1)]

        for a in A:
            for i in range(a, s/2 + 1):
                d[i] = max(d[i], d[i - a] + a) 
        return s - 2 * d[s / 2]

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 2, 3, 4, 5])
