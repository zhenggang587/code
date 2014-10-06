import math

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def shortestDist(self, points, l, r):
        if l == r:
            return 0.0
        if l == r - 1:
            return self.dist(points[l], points[r])
            
        m = (l + r) >> 1
        ld = self.shortestDist(points, l, m)
        rd = self.shortestDist(points, m + 1, r)

        minDist = min(ld, rd)
        tmpP = []
        for i in range(l, r + 1):
            if abs(points[i].x - points[m].x) <= minDist:
                tmpP.append(points[i])

        tmpP = sorted(tmpP, key=lambda p : p.y)
        for i in range(len(tmpP)):
            for j in range(i + 1, len(tmpP)):
                if abs(tmpP[j].y - tmpP[i].x) > minDist:
                    continue
                d = self.dist(tmpP[i], tmpP[j])
                minDist = min(minDist, d)
        return minDist

    def dist(self, p1, p2):
        px = p1.x - p2.x
        py = p1.y - p2.y
        return math.sqrt(px * px + py *py)


if __name__ == "__main__":
    s = Solution()

    points = [Point(), Point(1, 1), Point(0, 1), Point(1, 0)]
    points = sorted(points, key=lambda p : p.x)
    print s.shortestDist(points, 0, len(points) - 1)

    
