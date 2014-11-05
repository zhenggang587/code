
class Solution:
    def getSolution(self, n):
        if n % 2 != 0:
            return 0.0

        i = j = k = 1
        k = 1.0
        while i <= n / 2:
            j *= i
            k *= (i + n / 2)
            i += 1

        return k / j / pow(2, n)
        


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(4)
