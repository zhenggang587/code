
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0
        d = [0 if s[i] == '0' else 1 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] != '0':
                d[i] = d[i - 1] 
            else:
                d[i] = 0
            num = int(s[i-1:i+1])
            if s[i - 1] != '0' and num > 0 and num <= 26:
                if i >= 2:
                    d[i] += d[i - 2]    
                else:
                    d[i] += 1

        return d[len(s) - 1]



if __name__ == "__main__":
    s = Solution()

    print s.numDecodings('')
    print s.numDecodings('0')
    print s.numDecodings('101')
    print s.numDecodings('12')
    print s.numDecodings('123')
    print s.numDecodings('1213')
