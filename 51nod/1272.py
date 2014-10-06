
class Solution:
    def getSolution(self, A):
        stack = [0]
        n = len(A)
        for i in range(1, n):
            if A[i] < A[stack[-1]]:
                stack.append(i)

        ret = 0
        for i in range(n - 1, -1, -1):
            while stack:
                j = stack[-1]
                if A[j] > A[i]:
                    break
                stack.pop()
                ret = max(ret, i - j)
            if not stack:
                break

        return ret




if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([5, 3, 6, 3, 4, 2])
