
class Solution:
    def getSolution(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
