import math

class Solution:
    def getSolution(self, num):
        factors = []
        self.traverse(num, [], factors)
        factors.pop(0)
        return factors

    def traverse(self, num, factor, factors):
        if num == 1:
            return

        factor.append(num)
        factors.append(factor[:])
        factor.pop()

        k = int(math.sqrt(num)) + 1
        for i in range(2, k):
            if num % i == 0:
                if factor and i < factor[-1]:
                    continue
                factor.append(i)
                self.traverse(num / i, factor, factors)
                factor.pop()
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(16)
