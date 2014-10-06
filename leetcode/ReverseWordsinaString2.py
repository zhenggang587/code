
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s[::-1]

        start = -1
        end = 0
        ret = ''
        while end < len(s):
            if s[end] != ' ':
                if start == -1:
                    start = end
            else:
                if start != -1:
                    ret += self.reverse(s[start:end]) + ' '
                    start = -1
            end += 1
        if start != -1:
            ret += self.reverse(s[start:]) + ' '
                
        return ret[:-1]

    def reverse(self, s):
        return s[::-1]

     
if __name__ == "__main__":
    s = Solution()

    print len(s.reverseWords('  '))
