
class Solution:
    def getSolution(self, list):
        if not list or not list[0]:
            return None

        total = len(list) * len(list[0])
        l = 0
        r = (1 << 31) - 1
        while l <= r:
            m = l + (r - l) / 2
            cnt = self.judge(m, list)
            if cnt == total / 2:
                return m
            elif cnt > total / 2:
                r = m - 1
            else:
                l = m + 1
        return None

    def judge(self, num, list):
        p = len(list)
        n = len(list[0])
        lesscnt = 0
        lessthancnt = 0
        for i in range(p):
            for j in range(n):
                if list[i][j] < num:
                    lesscnt += 1
                if list[i][j] <= num:
                    lessthancnt += 1

        if lesscnt <= n * p / 2 and lessthancnt >= n * p / 2:
            return n * p / 2
        elif lessthancnt < n * p / 2:
            return lessthancnt
        else:
            return lesscnt
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 3, 4], [2, 5, 7], [2, 3, 4]])
