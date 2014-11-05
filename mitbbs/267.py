import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def __str__(self):
        return str(self.x) + ':' + str(self.y)

class Solution:
    def getSolution(self, points, k):
        if not points:
            return None

        points = sorted(points, key=lambda p : p.angle())

        fast = slow = 0
        cnt = maxCnt = 1
        maxStart = maxEnd = -1
        while fast < len(points) - 1:
            fast += 1
            cnt += 1
            while fast > slow and points[fast].angle() - points[slow].angle() > k:
                slow += 1
                cnt -= 1
            if cnt > maxCnt:
                maxCnt = cnt
                maxStart = slow
                maxEnd = fast

        return points[maxStart], points[maxEnd]


if __name__ == "__main__":
    s = Solution()
    
    r = s.getSolution([Point(1, 1), Point(-1, 2), Point(2, 3)], 30)
    for i in r:
        print i
