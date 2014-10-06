
# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

INT_MAX = (1 << 31) - 1
INT_MIN = -(1 << 31)

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points:
            return 0
        d = {}
        point_cnt = {}
        for p1 in points:
            cnt = 0
            if p1 in point_cnt:
                cnt = point_cnt[p1]
            point_cnt[p1] = cnt + 1

        if len(point_cnt) == 1:
            return 1

        upoints = point_cnt.keys()
        for i in range(len(upoints) - 1):
            for j in range(i + 1, len(upoints)):
                (k, b) = self.getLine(upoints[i], upoints[j])
                point_set = set()
                if (k, b) in d:
                    point_set = d[(k, b)]
                point_set.add(upoints[i])
                point_set.add(upoints[j])
                d[(k, b)] = point_set

        max_cnt = INT_MIN
        for point_set in d.values():
            cnt = 0
            for p in point_set:
                cnt += point_cnt[p]
            if cnt > max_cnt:
                max_cnt = cnt
        return max_cnt
                        
    def getLine(self, p1, p2):
        if p1.x == p2.x:
            return (INT_MAX, p1.x)

        k = float(p1.y - p2.y) / (p1.x - p2.x)
        b = p2.y - k * p2.x
        return (k, b)
        
     
if __name__ == "__main__":
    s = Solution()

    p1 = Point()
    p2 = Point(1, 1)
    p3 = Point(0, 1)
    p4 = Point(1, 0)
    p5 = Point(1, 0)

    print s.maxPoints([p1, p2, p3, p4, p5])
