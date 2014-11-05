import heapq

class Solution:
    def getSolution(self, A, k):
        h = []
        ret = []
        for i in range(len(A)):
            if i < k:
                heapq.heappush(h, A[i])
            else:
                ret.append(heapq.heappop(h))
                heapq.heappush(h, A[i])

        while h:
            ret.append(heapq.heappop(h))
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([2, 1, 4, 3], 2)
