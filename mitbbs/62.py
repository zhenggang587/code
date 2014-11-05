import heapq

# compare with (0, 0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __cmp__(self, other):
        return abs(self.x) + abs(self.y) > abs(other.x) + abs(other.y)

    def __str__(self):
        return str(self.x) + ':' + str(self.y)

class Solution:
    def getSolution(self, points, k):
        q = []
        for p in points:
            if len(q) < k:
                heapq.heappush(q, p)
            else:
                if p < q[0]:
                    heaq.heappop(q)
                    heaq.heappush(q, p)
        return q

                
        

if __name__ == "__main__":
    s = Solution()
    
    r = s.getSolution([Point(1, 1), Point(-1, 2), Point(2, 3)], 2)
    for i in r:
        print i
