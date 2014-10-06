
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

        
if __name__ == "__main__":
    s = Solution()

    assert s.isPalindrome("A man, a plan, a canal: Panama")==True
    assert s.isPalindrome("race a car")==False
