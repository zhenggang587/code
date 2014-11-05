
# assume query times is very big, so need preprocess

class Solution:
    def __init__(self, intervals):
        intervals.sort()

        i = 1
        while i < len(intervals):
            if intervals[i][0] > intervals[i - 1][0]:
                i += 1
            else:
                if intervals[i][1] > intervals[i - 1][1]:
                    intervals[i - 1][1] = intervals[i][1]
                intervals.pop(i)

        self.intervals = intervals

    def find(self, x):
        l = 0
        r = len(self.intervals) - 1
        while l <= r:
            m = l + (r - l) / 2
            if x >= self.intervals[m][0] and x <= self.intervals[m][1]:
                return True
            elif x < self.intervals[m][0]:
                r = m - 1
            else:
                l = m + 1
        return False


if __name__ == "__main__":
    s = Solution([[1, 10], [8, 12], [15, 20]])
    
    print s.find(-1)
    print s.find(11)
    print s.find(13)
