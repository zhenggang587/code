
# see 209.py

class Solution:
    def getSolution(self, A):
        n = len(A)
        ret = 0
        for i in range(n):
            ret ^= (A[i] ^ (i + 1))
        ret ^= n
        return ret



if __name__ == "__main__":
    s = Solution()

    print s.getSolution([1, 2, 1, 3])
