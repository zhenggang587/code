INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if len(str) == 0:
            return 0

        i = 0
        sign = 1
        if str[i] == '+':
            i = i + 1
        elif str[i] == '-':
            i = i + 1
            sign = -1

        ret = 0
        while i < len(str):
            if str[i] >= '0' and str[i] <= '9':
                ret = (ret * 10) + int(str[i])
                i = i + 1
            else:
                break

        if ret != 0 and sign == -1:
            ret = -ret

        if ret > INT_MAX:
            return INT_MAX
        elif ret < INT_MIN:
            return INT_MIN
        else:
            return ret

        

if __name__ == "__main__":
    s = Solution()
    print s.atoi('')
    print s.atoi(' -30')
    print s.atoi(' +30 20')
    print s.atoi(' 352e0 20')
    print s.atoi(' 322222222222222220')
