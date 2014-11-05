import random

class Solution:
    def getSolution(self, n, e):
        r = [0 for i in range(len(e))]
        for i in range(len(e)):
            r[i] = e[i] - i

        k = random.randint(1, n - len(r))
        i = 0
        j = len(r) - 1
        while i <= j:
            m = i + (j - i) / 2
            if r[m] <= k:
                i = m + 1
            else:
                j = m - 1

        return k + j + 1

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(10, [1, 5, 6])
    print s.getSolution(10, [1, 5, 6])
    print s.getSolution(10, [1, 5, 6])
    print s.getSolution(10, [1, 5, 6])
    print s.getSolution(10, [1, 5, 6])
    print s.getSolution(10, [1, 5, 6])
    print s.getSolution(10, [1, 5, 6])
    print s.getSolution(10, [1, 5, 6])
    print s.getSolution(10, [1, 5, 6])
