
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Solution:
    def getSolution(self, points):
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                samePoint = 0
                for k in range(j + 1, len(points)):
                    if self.isSame(points[i], points[k]) or self.isSame(points[j], points[k]):
                        samePoint += 1
                        continue

                        
                    

    def isSame(self, p1, p2):
        return p1.x == p2.x and p1.y == p2.y and p1.z == p2.z


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
