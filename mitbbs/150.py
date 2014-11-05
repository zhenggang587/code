
class Solution:
    def getSolution(self, A):
        m = {0 : -1}
        zeroSum = 0
        oneSum = 0
        maxSize = 0
        maxIndex = (-1, -1)
        for i in range(len(A)):
            if A[i] == 0:
                zeroSum += 1
            else:
                oneSum += 1
            diff = zeroSum - oneSum
            if diff not in m:
                m[diff] = i
            else:
                if i - m[diff] > maxSize:
                    maxSize = i - m[diff]
                    maxIndex = (m[diff] + 1, i)
        return maxIndex


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([0, 0, 1, 1, 0])
