
class Solution:
    def getSolution(self, s1, s2):
        if not s2:
            return [i for i in range(len(s1))]

        j = 0
        ret = []
        for i in range(len(s1)):
            if j >= len(s2) or s1[i] != s2[j]:
                ret.append(i)
            else:
                j += 1
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('abc', 'ac')
