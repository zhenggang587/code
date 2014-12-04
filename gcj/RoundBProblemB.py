
'''
1   1
3   2
6   3
10  4   
f(n) - f(n - 1) = n
=> f(n) = n * (n + 1) / 2
'''
class Solution:
    def getSolution(self, B, L, N):
        g, G = 250.0, 750.0 * B
        if L == 1:
            return min(g, G)

        a = [0, G - g]
        for i in range(1, L):
            # next level glass number
            n = (i + 1) * (i + 2) / 2
            b = [0 for j in range(n + 1)]
            # current level
            l = 1
            for k in range(1, len(a)):
                while k > l * (l + 1) / 2:
                    l += 1
                offset = l * (l + 1) / 2 + (k - l * (l - 1) / 2)
                b[k] += a[k] / 3
                b[offset] += a[k] / 3
                b[offset + 1] += a[k] / 3
            if i == L - 1:
                return b[N] if b[N] <= g else  g
            for j in range(len(b)):
                if b[j] <= g:
                    b[j] = 0
                else:
                    b[j] -= g

            a = b


if __name__ == "__main__":
    s = Solution()

    print s.getSolution(1, 2, 1)
    print s.getSolution(1, 1, 1)
    print s.getSolution(2, 1, 1)
    print s.getSolution(20, 1, 1)
    print s.getSolution(1, 3, 1)
    print s.getSolution(2, 3, 1)
    print s.getSolution(10, 4, 10)

