
class Solution:
    def getSolution(self, A):
        n = len(A)
        ret = [0 for i in range(n)]
        for i in range(n):
            ret[i % (n / 2) * (n / 2) + i / (n / 2)] = A[i]
        return ret

if __name__ == '__main__':
    s = Solution()

    print s.getSolution([1, 2, 3, 4, 5, 6])
