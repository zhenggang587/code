
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def getSolution(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x : x.end)

        second = intervals[0].end
        first = second - 1
        total = [first, second]
        for i in range(1, len(intervals)):
            if second < intervals[i].start:
                second = intervals[i].end
                first = second - 1
                total.append(first)
                total.append(second)
            elif first < intervals[i].start:
                first = second
                second = intervals[i].end
                total.append(second)

        return total

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([Interval(1, 4), Interval(2, 6), Interval(8, 9), Interval(1, 14)])
