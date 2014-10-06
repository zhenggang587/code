
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]

        ret = self.grayCode(n - 1)

        for i in range(len(ret) - 1, -1 , -1):
            ret.append((1 << (n - 1)) + ret[i])

        return ret
        
       
if __name__ == "__main__":
    s = Solution()

    print s.grayCode(3)
