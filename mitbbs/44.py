
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
        index = 1
        while index < len(intervals):
            if intervals[index - 1].end <= intervals[index].start:
                index += 1
            else:
                if intervals[index].end > intervals[index - 1].end:
                    intervals[index - 1].end = intervals[index].end
                intervals.pop(index)
        return len(intervals)
        
if __name__ == "__main__":
    s = Solution()

    l = []
    l.append(Interval(1, 4))
    l.append(Interval(4, 5))
    print s.merge(l)
