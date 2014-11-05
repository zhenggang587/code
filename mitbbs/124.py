
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution:
    def getSolution(self, points):
        return self.getXMedian(points, 0, len(points) - 1, len(points) / 2 + 1)

    def getXMedian(self, points, l, r, k):
        if l > r:
            return None

        i = l
        j = r
        key = points[i].x

        while i < j:
            while i < j and points[j].x >= key:
                j -= 1
            points[i].x = points[j].x
            while i < j and points[i].x <= key:
                i += 1
            points[j].x = points[i].x
        points[i].x = key

        m = i - l + 1
        if m == k:
            return points[i].x
        elif m > k:
            return self.getXMedian(points, l, i - 1, k)
        else:
            return self.getXMedian(points, i + 1, r, k - m)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([Point(1, 1), Point(2, 3), Point(10, 5)])
