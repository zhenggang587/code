
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def getSolution(self, intervals):
        if not intervals:
            return
        intervals = sorted(intervals, key=lambda x : x.end)

        interval = intervals[0]
        ret = [(interval.start, interval.end)]
        for i in range(1, len(intervals)):
            if intervals[i].start > interval.end:
                ret.append((intervals[i].start, intervals[i].end))
                interval = intervals[i]
            i += 1
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([Interval(1, 4), Interval(2, 6), Interval(8, 9), Interval(1, 14)])
