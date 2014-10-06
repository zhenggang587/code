
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        ret = []
        subset = []
        self.getPalindrome(s, 0, subset, ret)
        return ret

    def getPalindrome(self, s, index, subset, ret):
        if index == len(s):
            ret.append(subset[:])
            return

        for i in range(index, len(s)):
            left_str = s[index:i+1] 
            if self.isPalindrome(left_str):
                subset.append(left_str)
                self.getPalindrome(s, i + 1, subset, ret)
                subset.pop()

    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()

    print s.partition('aaaa')
