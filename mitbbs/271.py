
# see 62.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return self.x * self.x + self.y * self.y

    def __str__(self):
        return str(self.x) + ':' + str(self.y)

class Solution:
    def getSolution(self, points, k):
        self.partition(points, 0, len(points) - 1, k)
        return points[:k]

    def partition(self, points, l, r, k):
        i = l
        j = r
        p = points[i]
        while i < j:
            while i < j and points[j].dist() >= p.dist():
                j -= 1
            points[i] = points[j]
            while i < j and points[i].dist() <= p.dist():
                i += 1
            points[j] = points[i]
        points[i] = p

        m = i - l + 1
        if m == k:
            return
        elif m > k:
            self.partition(points, l, i, k)
        else:
            self.partition(points, i + 1, r, k - m)
            


if __name__ == "__main__":
    s = Solution()
    
    r = s.getSolution([Point(1, 1), Point(-1, 2), Point(2, 3)], 3)
    for i in r:
        print i
