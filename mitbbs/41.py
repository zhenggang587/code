
class Solution:
    def getSolution(self, dict, s):
        wordSet = set()
        for d in dict:
            wordSet.add(''.join(sorted(d)))

        n = len(s)
        maxLen = 0
        state = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                sub = ''.join(sorted(s[i:j+1]))
                if sub in wordSet:
                    state[i][j] = True
                    if maxLen < j - i + 1:
                        maxLen = j - i + 1

        d = [i for i in range(n + 1)]
        for i in range(n):
            k = max(0, i - maxLen + 1)
            for j in range(k, i + 1):
                temp = d[j]
                if not state[j][i]:
                    temp += i - j + 1
                if temp < d[i + 1]:
                    d[i + 1] = temp
        return d[n]
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(['window', 'cat'], 'iwndowdcta')
