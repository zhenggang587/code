
# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

INT_MAX = (1 << 31) - 1

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)

        ret = 0
        for i in range(len(points) - 1):
            same_point = 0
            line = {}
            point_max = 1
            for j in range(i + 1, len(points)):
                if points[i].x == points[j].x:
                    if points[i].y == points[j].y:
                        same_point += 1
                        continue
                    k = INT_MAX 
                else:
                    k = float(points[i].y - points[j].y) / (points[i].x - points[j].x)

                if k not in line:
                    line[k] = 2
                else:
                    line[k] += 1
                point_max = max(point_max, line[k])

            ret = max(ret, point_max + same_point)
        return ret
                
     
if __name__ == "__main__":
    s = Solution()

    p1 = Point()
    p2 = Point(1, 1)
    p3 = Point(0, 1)
    p4 = Point(1, 0)
    p5 = Point(1, 0)

    print s.maxPoints([p1, p2, p3, p4, p5])
