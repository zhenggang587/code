
class Solution:
    def getSolution(self, A):
        n = len(A)
        maxC = 0
        for i in range(n):
            fast = slow = i
            while A[fast] != -1 and A[A[fast]] != -1:
                slow = A[slow]
                fast = A[A[fast]]
                if slow == fast:
                    fast = A[fast]
                    cycleLen = 1
                    while fast != slow:
                        fast = A[fast]
                        cycleLen += 1
                    maxC = max(maxC, cycleLen)
                    break
        return maxC
                    

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([3, 2, 1, 4, 0])
