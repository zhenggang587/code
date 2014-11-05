import random

class Solution:
    def unfair(self):
        if random.randint(1, 4) == 1:
            return True
        else:
            return False

    def getSolution(self):
        a = self.unfair()
        b = self.unfair()
        if a == True and b == False:
            return True
        elif a == False and b == True:
            return False
        return self.getSolution()

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
    print s.getSolution()
    print s.getSolution()
    print s.getSolution()
    print s.getSolution()
