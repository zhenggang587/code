
# majority number
class Solution:
    def getSolution(self, A):
        if not A:
            return -1

        ret = None
        cnt = 0
        for a in A:
            if cnt == 0:
                ret = a
            if ret == a:
                cnt += 1
            else:
                cnt -= 1
        return ret
                

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([2, 2, 3])
