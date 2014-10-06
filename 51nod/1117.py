import heapq

class Solution:
    def getSolution(self, list):
        q = [] 
        for l in list:
            heapq.heappush(q, l)

        ret = 0
        while len(q) > 1:
           sum = heapq.heappop(q)
           sum += heapq.heappop(q)
           ret += sum
           heapq.heappush(q, sum)
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([5, 4, 3])
