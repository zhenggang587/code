
class Solution:
    def getSolution(self, s):
        next = self.getNext(s)
        n = len(s)
        i = 0
        while i < n and next[i] == -1:
            i += 1

        K = i
        j = 0
        while i < n and next[i] == j:
            i += 1
            j += 1
        if i == n and n % K == 0:
            return True
        return False

    def getNext(self, s):
        n = len(s)
        next = [-1 for i in range(n)]

        j = -1
        for i in range(1, n):
            if j >= 0 and s[i] != s[j + 1]:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j
        return next

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('aaaa')
    print s.getSolution('abcabc')
    print s.getSolution('abcabcab')
