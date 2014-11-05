
# l[i] = max(l[j] + 1, A[j] <= A[i] and j < i)
class Solution:
    def getSolution(self, A):
        if not A:
            return 0

        n = len(A)
        l = [1 for i in range(n)]
        ret = 1
        for i in range(1, n):
            for j in range(i):
                if A[j] <= A[i]:
                    l[i] = max(l[i], l[j] + 1)
            ret = max(ret, l[i])
        return ret

    def getSolution1(self, A):
        l = [A[0]]
        for k in range(1, len(A)):
            i = 0
            j = len(l) - 1
            while i <= j:
                m = i + (j - i) / 2
                if A[k] >= l[m]:
                    i = m + 1
                else:
                    j = m - 1
            if i >= len(l):
                l.append(A[k])
            else:
                l[i] = A[k]
        return len(l)


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution1([5, 1, 6, 8, 2, 4, 5, 10])
