
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'

class Solution:
    def getSolution(self, intervals):
        queue = []
        for i in intervals:
            queue.append((i.start, 0))
            queue.append((i.end, 1))
        queue.sort()

        cnt = 0
        maxCnt = 0
        maxP = None
        for p, s in queue:
            if s == 0:
                cnt += 1
                if cnt > maxCnt:
                    maxCnt = cnt
                    maxP = p
            else:
                cnt -= 1
        return maxP
            

class Solution1:
    def getSolution(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        points = []
        for i in intervals:
            points.append(i.start)
            points.append(i.end)

        maxCnt = 0
        maxP = None
        for p in points:
            cnt = 0
            for i in intervals:
                if p >= i.start and p <= i.end:
                    cnt += 1
                elif p < i.start:
                    break
            if cnt > maxCnt:
                maxCnt = cnt
                maxP = p
        return maxP
                    

if __name__ == "__main__":
    s = Solution()
    
    l = []
    l.append(Interval(1, 3))
    l.append(Interval(2, 6))
    l.append(Interval(8, 10))
    l.append(Interval(9, 18))
    l.append(Interval(10, 18))
    print s.getSolution(l)
