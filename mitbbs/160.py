
class Solution:
    def getSolution(self, A):
        n = len(A)
        l = [0 for i in range(n)]
        minLeft = A[0]
        minIndex = 0
        for i in range(n):
            if A[i] < minLeft:
                minLeft = A[i]
                minIndex = i
            l[i] = minIndex
            
        r = [n - 1 for i in range(n)]
        maxRight = A[n - 1]
        maxIndex = n - 1
        for i in range(n - 1, -1, -1):
            if A[i] > maxRight:
                maxRight = A[i]
                maxIndex = i
            r[i] = maxIndex

        for i in range(1, n - 1):
            if A[l[i]] < A[i] and A[i] < A[r[i]]:
                return l[i], i, r[i]
        return None
    
if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 5, 4, 6])
