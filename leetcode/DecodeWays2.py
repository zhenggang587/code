
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0

        d = [0 for i in range(len(s) + 1)]
        d[0] = 1
        d[1] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if s[i] != '0':
                d[i + 1] = d[i]
            num = int(s[i-1:i+1])
            if num > 0 and num <= 26 and s[i - 1] != '0':
                d[i + 1] += d[i - 1]

        return d[len(s)]



if __name__ == "__main__":
    s = Solution()

    print s.numDecodings('')
    print s.numDecodings('0')
    print s.numDecodings('101')
    print s.numDecodings('12')
    print s.numDecodings('123')
    print s.numDecodings('1213')
