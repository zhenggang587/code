
class Solution:
    def getSolution(self, s):
        m = {}
        for c in s:
            if c not in m:
                m[c] = 0
            m[c] += 1

        ret = ''
        for c, cnt in m.items():
            if cnt % 2 == 1:
                ret += c
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('abaadefbe')
