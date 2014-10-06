
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        s = sorted(S)

        ret = []
        n = len(s)
        total = 1 << n
        for i in range(total):
            tmp = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    tmp.append(s[j])
            ret.append(tmp)
        return ret

        
if __name__ == "__main__":
    s = Solution()

    print s.subsets([1, 2, 3])

