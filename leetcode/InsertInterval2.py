
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
        index = 0
        while index < len(intervals):
            if newInterval.start > intervals[index].end:
                index += 1
            elif newInterval.end < intervals[index].start:
                intervals.insert(index, newInterval)
                return intervals
            else:
                if intervals[index].start < newInterval.start:
                    newInterval.start = intervals[index].start
                if intervals[index].end > newInterval.end:
                    newInterval.end = intervals[index].end
                intervals.pop(index)

        intervals.append(newInterval)
        return intervals
        
        
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

