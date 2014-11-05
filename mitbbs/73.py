import time

class Solution:
    def __init__(self):
        self.m = {}
        self.allValue = None
        self.allTime = 0
        
    def getValue(self, index):
        if index not in self.m:
            return None

        v, t = self.m[index]
        if t < self.allTime:
            return self.allValue
        else:
            return v

    def setValue(self, index, value):
        self.m[index] = (value, time.time()) 
        

    def setAllValue(self, value):
        self.allValue = value
        self.allTime = time.time()


if __name__ == "__main__":
    s = Solution()
    
    s.setValue(1, 5)
    s.setValue(2, 3)
    print s.getValue(1)
    s.setAllValue(0)
    print s.getValue(2)
