
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        next = self.getNext(needle)
        j = -1
        for i in range(len(haystack)):
            while j != -1 and haystack[i] != needle[j + 1]:
                j = next[j]
            if haystack[i] == needle[j + 1]:
                j += 1

            if j == len(needle) - 1:
                return i - j
        return -1

    def getNext(self, needle):
        next = [-1 for i in range(len(needle))]
        j = -1
        for i in range(1, len(needle)):
            while j != -1 and needle[i] != needle[j + 1]:
                j = next[j]
            if needle[i] == needle[j + 1]:
                j += 1
                next[i] = j

        return next
        
if __name__ == "__main__":
    s = Solution()

    print s.strStr('mississippi', 'issip')
    print s.getNext('aaabaaab')
