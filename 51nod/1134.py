
class Solution:
    def getSolution(self, A):
        l = [1 for a in A]
        ret = 1
        n = len(A)
        for i in range(n):
            for j in range(i):
                if A[j] < A[i]:
                    l[i] = max(l[i], l[j] + 1)
            ret = max(ret, l[i])
        return ret

    def getSolution1(self, A):
        l = [A[0]]
        ret = 1
        n = len(A)
        for i in range(1, n):
            p = self.find(l, A[i])
            if p >= len(l):
                l.append(A[i])
                ret = max(ret, len(l))
            else:
                l[p] = A[i]
        return ret

    def find(self, A, x):
        l = 0
        r = len(A) - 1
        while l <= r:
            m = l + (r - l) / 2
            if A[m] == x:
                return m
            elif A[m] > x:
                r = m - 1
            else:
                l = m + 1
        return l 




if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution1([5, 1, 6, 8, 2, 4, 5, 10])
