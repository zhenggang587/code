
class Solution:
    def getSolution(self, S, T):
        next = self.getNext(S)

        j = -1
        m = len(T)
        n = len(S)
        cnt = 0
        for i in range(m):
            while j >= 0 and T[i] != S[j + 1]:
                j = next[j]
            if T[i] == S[j + 1]:
                j += 1

            if j == n - 1:
                j = next[j]
                cnt += 1
        return cnt

    def getNext(self, s):
        n = len(s)
        next = [-1 for i in range(n)]
        j = -1
        for i in range(1, n):
            while j >= 0 and s[i] != s[j + 1]:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j
        return next

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('aba', 'ababa')
