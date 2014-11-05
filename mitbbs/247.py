
class Solution:
    def getSolution(self, A, swapTime):
        n = swapTime
        for i in range(len(A)):
            maxNum = maxIndex = -1
            l = min(len(A), i + n + 1)
            for j in range(i, l):
                if A[j] > maxNum:
                    maxNum = A[j]
                    maxIndex = j
            A = A[:i] + [A[maxIndex]] + A[i:maxIndex] + A[maxIndex + 1:]
            n -= maxIndex - i
        return A
         

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 2, 3], 3)
