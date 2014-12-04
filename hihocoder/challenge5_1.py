
class Solution:
    def getSolution(self, A):
        n = len(A)
        leftStack = [A[0]]
        leftLower = [False for i in range(n)]
        for i in range(1, n):
            while leftStack:
                if leftStack[-1] > A[i]:
                    leftStack.pop()
                else:
                    break
            if leftStack:
                leftLower[i] = True
            leftStack.append(A[i])

        leftStack = [A[0]]
        leftUpper = [False for i in range(n)]
        for i in range(1, n):
            while leftStack:
                if leftStack[-1] < A[i]:
                    leftStack.pop()
                else:
                    break
            if leftStack:
                leftUpper[i] = True
            leftStack.append(A[i])

        rightStack = [A[n - 1]]
        rightLower = [False for i in range(n)]
        for i in range(n - 2, -1, -1):
            while rightStack:
                if rightStack[-1] > A[i]:
                    rightStack.pop()
                else:
                    break
            if rightStack:
                rightLower[i] = True
            rightStack.append(A[i])

        rightStack = [A[n - 1]]
        rightUpper = [False for i in range(n)]
        for i in range(n - 2, -1, -1):
            while rightStack:
                if rightStack[-1] < A[i]:
                    rightStack.pop()
                else:
                    break
            if rightStack:
                rightUpper[i] = True
            rightStack.append(A[i])

        ret = []
        for i in range(n):
            if (leftLower[i] and rightUpper[i]) or (leftUpper[i] and rightLower[i]):
                continue
            ret.append(i + 1)
        return ret




if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 2, 3, 4, 3, 2, 3, 4, 5, 4])
