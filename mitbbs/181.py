
class Solution:
    def getSolution(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True

        if n % 3 != 0:
            return False
        return self.getSolution(n / 3)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(8)
