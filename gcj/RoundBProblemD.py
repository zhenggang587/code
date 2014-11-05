
class Solution:
    def GetSolution(self, n, k):
        h = [0 for i in range(n + 1)]
        h[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                h[i] += h[j] * h[i - j - 1]

        return self.getSolution(n, k - 1, h)

    def getSolution(self, n, k, h):
        if n <= 0:
            return ''
        if k == 0:
            return '(' * n + ')' * n
        

        if k >= h[n]:
            return None

        base = h[n - 1] * h[0]
        left = n - 1
        right = 0
        while k >= h[left] * h[right]:
            k -= h[left] * h[right]
            left -= 1
            right += 1

        return '(' + self.getSolution(left, k / h[right], h) + ')' + self.getSolution(right, k % h[right], h)


    def getParentheses(self, n):
        if n == 0:
            return ['']

        ret = []
        for i in range(n - 1, -1, -1):
            left = self.getParentheses(i)
            right = self.getParentheses(n - i - 1)
            for l in left:
                for r in right:
                    ret.append('(' + l + ')' + r)
        return ret
            


if __name__ == "__main__":
    s = Solution()

    ret = s.getParentheses(5)
    print ret[20]
    print s.GetSolution(5, 21)
