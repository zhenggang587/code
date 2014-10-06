
# TLE, see c++

class Solution:
    # @return a string
    def longestPalindrome(self, s): 
        maxLen = 0
        startPos = 0
        for i in range(len(s)):
            
            oddLen = self.getPalindrome(s, i, i)
            curLen, evenLen = 0, 0
            if i + 1 < len(s):
                evenLen = self.getPalindrome(s, i, i + 1)
            curLen = max(oddLen, evenLen)
            if curLen > maxLen:
                maxLen = curLen
                if curLen % 2 == 1:
                    startPos = i - curLen / 2
                else:
                    startPos = i - curLen / 2 + 1

        return s[startPos:maxLen]

    def getPalindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return (j - 1) - (i + 1) + 1
        

if __name__ == "__main__":
    s = Solution()

    print s.longestPalindrome('abc')
