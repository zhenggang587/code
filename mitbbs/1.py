
# another method: use suffix tree

class Solution:
    def getSolution(self, s):
        n = len(s)
        l = n - 1
        for l in range(n - 1, 0, -1):
            m = set()
            for i in range(0, n - l + 1):
                if s[i:i+l] not in m:
                    m.add(s[i:i+l])
                else:
                    return s[i:i+l]
        return ''


if __name__ == "__main__":
    s = Solution()
    
    #print s.getSolution('abcabcaacb')
    print s.getSolution('aababa')
