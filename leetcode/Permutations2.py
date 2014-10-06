
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if not num:
            return []

        n = len(num)
        ret = [[num[0]]]
        for i in range(1, n):
            new = []
            for p in ret:
                for j in range(i + 1):
                    new.append(p[:j] + [num[i]] + p[j:])
            ret = new

        return ret
        
        
if __name__ == "__main__":
    s = Solution()

    print s.permute([1, 2, 3])
