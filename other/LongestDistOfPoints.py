
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __cmp__(self, other):
        d = multiply(self, other, p0)
        if d > 1e-6:
            return -1
        elif abs(d) <= 1e-6:
            return 0
        return 1

p0 = None

def multiply(p1, p2, p0):
    return (p1.x - p0.x) * (p2.y - p0.y) - (p2.x - p0.x) * (p1.y - p0.y)

class Solution:
    def getSolution(self, points):
        n = len(points)

        t = 0
        for i in range(1, n):
            if points[i].x < points[t].x or (points[i].x == points[t].x and points[i].y < points[t].y):
                t = i
        points[t], points[0] = points[0], points[t]

        global p0
        p0 = points[0]
        points = sorted(points[1:]) 
        points.insert(0, p0)

        if n < 3:
            return

        h = [None for i in range(n)]
        h[0], h[1], h[2] = [points[0], points[1], points[2]]
        top = 2
        for i in range(3, n):
            while multiply(points[i], h[top], h[top - 1]) >= 0:
                top -= 1
                if top == 0:
                    break
            top += 1
            h[top] = points[i]
        return h[:top+1]
    

if __name__ == "__main__":
    s = Solution()

    points = [Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 0), Point(0.5, 0.5), Point(5, 5)]
    h = s.getSolution(points)
    for p in h:
        print p.x, p.y
