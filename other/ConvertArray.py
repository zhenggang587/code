
class Solution:
    def convert(self, A):
        N = len(A) / 3
        return [A[self.getIndex(i, N)] for i in range(len(A))]

    def convert1(self, A):
        N = len(A) / 3
        for i in range(len(A)):
            swapIndex = self.getIndex(i, N)
            while swapIndex < i:
                swapIndex = self.getIndex(swapIndex, N)
            A[swapIndex], A[i] = A[i], A[swapIndex]
            print A


    def getIndex(self, curIndex, N):
        return (curIndex % 3) * N + (curIndex / 3)
if __name__ == "__main__":
    s = Solution()

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #print s.convert(A)

    s.convert1(A)
    print A

