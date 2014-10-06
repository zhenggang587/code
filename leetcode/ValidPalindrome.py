
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            while not self.isAlphaNumberic(s[i]) and i < j:
                i += 1
            while not self.isAlphaNumberic(s[j]) and j > i:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

    def isAlphaNumberic(self, c):
        return (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')
        
if __name__ == "__main__":
    s = Solution()

    assert s.isPalindrome("A man, a plan, a canal: Panama")==True
    assert s.isPalindrome("race a car")==False
