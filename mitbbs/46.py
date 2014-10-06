
class Solution:
    def getSolution(self, s):
        n = len(s)
        index = 0
        pos = 0
        cnt = 0
        while index < n:
            if s[index] != 'A':
                s[pos] = s[index]
                pos += 1
                if s[index] == 'B':
                    cnt += 1
            index += 1

        n = pos
        nn = n + cnt
        pos = nn - 1
        index = n - 1
        while index >= 0:
            s[pos] = s[index]
            pos -= 1
            if s[index] == 'B':
                s[pos] = 'B'
                pos -= 1
            index -= 1 
        return s[:nn]


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(['C', 'B', 'B', 'A', 'A'])
