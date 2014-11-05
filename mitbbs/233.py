
class Solution:
    def getSolution(self, A):
        if len(A) <= 1:
            if A[0] > 3:
                return [A[0] * A[0] / 10, A[0] * A[0] % 10]
            return [A[0] * A[0]]

        n = len(A)
        m = n / 2
        l = self.getSolution(A[:m])
        r = self.getSolution(A[m:])

        ret = r

        tmp = self.multiply(A[:m], A[m:])
        tmp = self.add(tmp, tmp)
        tmp.extend([0] * (n - m))
        ret = self.add(ret, tmp)

        l.extend([0] * 2 * (n - m))
        return self.add(ret, l)


    def add(self, A, B):
        m = len(A)
        n = len(B)
        k = max(m, n) + 1
        ret = [0 for i in range(k)]
        i = m - 1
        j = n - 1

        borrow = 0
        k = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                borrow += A[i]
                i -= 1
            if j >= 0:
                borrow += B[j]
                j -= 1
            ret[k] = borrow % 10
            borrow /= 10
            k += 1
        if borrow:
            ret[k] = borrow
            k += 1
        ret = ret[::-1]
        for i in range(k):
            if ret[i] != 0:
                break
        return ret[i:]

    def multiply(self, A, B):
        m = len(A)
        n = len(B)
        ret = [0 for i in range(m + n)]
        for i in range(m):
            for j in range(n):
                sum = A[m - 1 - i] * B[n - 1 - j]
                k = i + j
                ret[k] += sum
                if ret[k] >= 10:
                    ret[k + 1] += ret[k] / 10
                    ret[k] %= 10

        ret = ret[::-1]
        for k in range(m + n):
            if ret[k] != 0:
                break
        return ret[k:]



if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 0, 0])
