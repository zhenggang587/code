
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def getSolution(self, points, p):
        n = len(points)
        i = 0
        j = n - 1
        c = False
        while i < n:
            if (points[i].y > p.y) != (points[j].y > p.y) and \
                (p.x < (points[j].x - points[i].x) * (p.y - points[i].y) / (points[j].y - points[i].y) + points[i].x):
                c = not c
            j = i
            i += 1
        return c

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)], Point(0.5, -0.5))

