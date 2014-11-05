import random

class Solution:
    def getSolution(self, n):
        A = [i for i in range(1, n + 1)]

        for i in range(1, n + 1):
            j = random.randint(1, i)
            A[i - 1], A[j - 1] = A[j - 1], A[i - 1]
        return A
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(3)
    print s.getSolution(3)
    print s.getSolution(3)
    print s.getSolution(3)
    print s.getSolution(3)
    print s.getSolution(3)
