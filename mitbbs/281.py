
# see 39.py

class Interval:
    def __init__(self, start, end, mem):
        self.start = start
        self.end = end
        self.mem = mem

class Solution:
    def __init__(self):
        self.taskMap = {}

    def submit(self, user, intervals):
        arr = []
        for interval in intervals:
            arr.append((interval.start, 0, interval.mem))
            arr.append((interval.end, 1, interval.mem))
        arr = sorted(arr)

        mem = 0
        maxMem = 0
        for elem in arr:
            if elem[1] == 0:
                mem += elem[2]
            else:
                mem -= elem[2]
            maxMem = max(maxMem, mem)
        
        self.taskMap[user] = maxMem

    def getMaxMem(self, user):
        if user not in self.taskMap:
            return 0
    
        return self.taskMap[user]


if __name__ == "__main__":
    s = Solution()

