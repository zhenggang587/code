import heapq

class Solution:
    def getSolution(self, A, B, m):
        ret = []
        q = [(A[0] + B[0], 0, 0)]
        while len(ret) < m:
            sum, i, j = heapq.heappop(q)
            ret.append((A[i], B[j]))
            if i + 1 < len(A) and (i + 1, j) not in q:
                heapq.heappush(q, (A[i + 1] + B[j], i + 1, j))
            if j + 1 < len(B) and (i, j + 1) not in q:
                heapq.heappush(q, (A[i] + B[j + 1], i, j + 1))
        return ret
                

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 2, 4, 5, 6], [3, 5, 7, 9], 3)
