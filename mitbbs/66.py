
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if not needle:
            return haystack

        next = self.getnext(needle)
        i = 0
        j = 0
        cnt = 0
        while i < len(haystack):
            while i < len(haystack) and j < len(needle):
                if j == -1 or haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    j = next[j]

            if j >= len(needle):
                cnt += 1
                j = 0
        return cnt 

    def getnext(self, needle):
        next = [-1 for i in range(len(needle))]
        j = -1
        i = 0
        while i < len(needle) - 1:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                if needle[i] != needle[j]:
                    next[i] = j
                else:
                    next[i] = next[j]
            else:
                j = next[j]

        return next
        
if __name__ == "__main__":
    s = Solution()

    print s.strStr('a', 'a')
