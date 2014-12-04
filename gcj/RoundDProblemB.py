
class Solution:
    def __init__(self, intervals):
        self.cnt = [0 for i in range(501)]
        for (s, e) in intervals:
            for i in range(s, e + 1):
                self.cnt[i] += 1
        
    def getSolution(self, querys):
        ret = []
        for q in querys:
            ret.append(self.cnt[q])
        return ret


if __name__ == "__main__":
    s = Solution([(15, 25), (30, 35), (45, 50), (10, 20)])
    print s.getSolution([15, 25])


    s = Solution([(10, 15), (5, 12), (40, 55), (1, 10), (25, 35), (45, 50), (20, 28), (27, 35), (15, 40), (4, 5)])
    print s.getSolution([5, 10, 27])
