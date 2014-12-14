
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if not num:
            return 0

        tmp = num
        for i in range(32):
            zero = []
            one = []
            for a in tmp:
                if a & (1 << i):
                    one.append(a)
                else:
                    zero.append(a)
            tmp = zero + one

        maxDiff = 0
        for i in range(1, len(tmp)):
            maxDiff = max(maxDiff, tmp[i] - tmp[i - 1])
        return maxDiff
            
     
if __name__ == "__main__":
    s = Solution()

    print s.maximumGap([3, 1, 4, 2, 20, 10])
