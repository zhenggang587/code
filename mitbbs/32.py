import heapq

class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insert(self, a):
        if not self.minHeap or a < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -a)
        else:
            heapq.heappush(self.minHeap, a)

        self.adjust()

    def adjust(self):
        if abs(len(self.minHeap) - len(self.maxHeap)) <= 1:
            return

        if len(self.minHeap) - len(self.maxHeap) > 1:
            v = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -v)
        else:
            v = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -v)

    def delete(self, a):
        if a < self.minHeap[0]:
            self.maxHeap.remove(-a)
        else:
            self.minHeap.remove(a)

        self.adjust()

    def getMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]

    def getSolution(self, A, k):
        ret = []
        for i in range(len(A)):
            self.insert(A[i])
            if i >= k:
                self.delete(A[i - k])
            if i >= k - 1:
                ret.append(self.getMedian())
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 4, 5, 7, 3, 5, 2, 9], 3)
