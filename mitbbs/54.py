
# three coke machine

class Solution:
    def getSolution(self, l, m, n):
        return self.traverse(l, [0, 0, 0], m, n)

    def traverse(self, l, k, m, n):
        x, y = 0, 0
        for i in range(3):
            x += l[i][0] * k[i]
            y += l[i][1] * k[i]
        if x >= m and y <= n:
            return True
        if x > n:
            return False

        for i in range(3):
            k[i] += 1
            if self.traverse(l, k, m, n):
                return True
            k[i] -= 1

        return False


if __name__ == "__main__":
    s = Solution()
    
    l = [[2, 5], [3, 4], [1, 4]]
    print s.getSolution(l, 20, 20)
