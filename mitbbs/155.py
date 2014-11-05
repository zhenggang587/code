import math

class Solution:
    def getSolution(self):
        return self.getPalindrome(1000000)

    def getPalindrome(self, n):
        ret = set()
        self.getOdd(n, ret)
        self.getEven(n, ret)

        return list(ret)
    
    def getOdd(self, n, ret):
        odd = [i for i in range(10)]
        power = 100
        while True:
            tmp = []
            for i in odd:
                if i > n:
                    return
                if self.isPrime(i):
                    ret.add(i)
                for j in range(10):
                    k = j * power + i * 10 + j
                    tmp.append(k)
            power *= 100
            odd = tmp

    def getEven(self, n, ret): # only 11
        even = [i * 10 + i for i in range(10)]
        power = 1000
        while True:
            tmp = []
            for i in even:
                if i > n:
                    return
                if self.isPrime(i):
                    ret.add(i)
                for j in range(10):
                    k = j * power + i * 10 + j
                    tmp.append(k)
            power *= 100
            even = tmp

    def isPrime(self, n):
        if n < 2:
            return False
        s = int(math.sqrt(n))
        for i in range(2, s + 1):
            if n % i == 0:
                return False
        return True
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
