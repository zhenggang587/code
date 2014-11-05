
# sliding window

class Solution:
    def getSolution(self, A, k):
        s = []
        ret = []
        for i in range(len(A)):
            while s and A[i] > A[s[-1]]:
                s.pop()
            s.append(i)
            if i >= k and s[0] <= i - k:
                s.pop(0)
            if i >= k - 1:
                ret.append(A[s[0]])
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 4, 5, 7, 3, 5, 2, 9], 1)
