
class Solution:
    def getSolution(self, s1, s2):
        if not s1 and not s2:
            return 0
        if not s1:
            return len(s2)
        if not s2:
            return len(s1)

        if s1[0] == s2[0]:
            return self.getSolution(s1[1:], s2[1:])
        else:
            return min(self.getSolution(s1[1:], s2), self.getSolution(s1, s2[1:]), self.getSolution(s1[1:], s2[1:])) + 1

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('', '')
    print s.getSolution('abc', '')
    print s.getSolution('', 'abc')
    print s.getSolution('abc', 'abc')
    print s.getSolution('abc', 'ad')
    print s.getSolution('abc', 'acd')
    print s.getSolution('abc', 'abceeeee')
    print s.getSolution('abc', 'bceeeee')
