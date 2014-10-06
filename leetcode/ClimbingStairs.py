
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 2:
            return n
        step = [1 for i in range(n)]
        step[1] = 2
        for i in range(2, n):
            step[i] = step[i - 1] + step[i - 2]

        return step[n - 1]
        
if __name__ == "__main__":
    s = Solution()

    print s.climbStairs(4)

