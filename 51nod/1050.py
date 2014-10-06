
class Solution:
    def work(self, A):
        b = A[0]
        ret = A[0]
        for i in range(1, len(A)):
            if b > 0:
                b += A[i]
            else:
                b = A[i]
            ret = max(ret, b)
        return ret
        
    def getSolution(self, A):
        ans1 = self.work(A)
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            A[i] = -A[i]
        ans2 = self.work(A)
        return max(ans1, sum + ans2)

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([-2,11,-4,13,-5,-2])
