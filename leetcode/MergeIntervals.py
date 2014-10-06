
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x : x.start)

        ret = []
        base = intervals[0]
        index = 1
        while index < len(intervals):
            if base.end < intervals[index].start:
                ret.append(base)
                base = intervals[index]
            elif base.end <= intervals[index].end:
                base.end = intervals[index].end

            index += 1
        if base and base.end >= intervals[len(intervals) - 1].end:
            ret.append(base)
        return ret
        
if __name__ == "__main__":
    s = Solution()

    l = []
    l.append(Interval(1, 4))
    ret = s.merge(l)
    for r in ret:
        print r
