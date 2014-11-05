
class Solution:
    def getSolution(self):
        ret = []
        for i in range(10):
            for j in range(10):
                if j == i:
                    continue
                num = 100 - (i * 10 + j)
                l = num / 10
                m = num % 10
                s = set([i, j, l, m])
                if len(s) == 4:
                    print i, j, l, m
                    ret.append((i, j, l, m))
        return len(ret)


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
