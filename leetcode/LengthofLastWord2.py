
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        for i in range(len(s)):
            if s[i] != ' ':
                if i - 1 >= 0 and s[i - 1] == ' ':
                    length = 0
                length += 1
            
        return length
        
        
if __name__ == "__main__":
    s = Solution()

    assert s.lengthOfLastWord('hello world') == 5
    assert s.lengthOfLastWord('   hello world   ') == 5
    assert s.lengthOfLastWord('helloworld') == 10
    assert s.lengthOfLastWord('') == 0

