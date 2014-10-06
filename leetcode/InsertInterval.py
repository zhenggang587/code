
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        ret = []
        index = 0
        min_start = newInterval.start
        while index < len(intervals):
            start = intervals[index].start 
            if start < min_start:
                min_start = start

            end = intervals[index].end
            if newInterval.start < start:
                if newInterval.end < start:
                    ret.append(Interval(min_start, newInterval.end))
                    break
                start = newInterval.start
            elif newInterval.start > end:
                ret.append(intervals[index])
                min_start = newInterval.start
                index += 1
                continue

            if newInterval.end <= end:
                ret.append(Interval(min_start, end))
                index += 1
                break
            else:
                index += 1

        if newInterval.end > intervals[len(intervals) - 1].end:
            ret.append(Interval(min_start, newInterval.end))
        ret.extend(intervals[index:])
        return ret
        
        
if __name__ == "__main__":
    s = Solution()

    i1 = Interval(1, 2)
    i2 = Interval(3, 5)
    i3 = Interval(6, 7)
    i4 = Interval(8, 10)
    i5 = Interval(12, 16)
    newi = Interval(0, 17)
    ret = s.insert([i1, i2, i3, i4, i5], newi)
    for r in ret:
        print r

