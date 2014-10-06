
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        last_length = 0
        length = 0
        index = 0
        start = -1
        while index < len(s):
            if s[index] != ' ':
                length += 1
                if index + 1 < len(s) and s[index + 1] == ' ':
                    last_length = length
                    length = 0
            index += 1

        if length > 0:
            return length
        return last_length
        
        
if __name__ == "__main__":
    s = Solution()

    assert s.lengthOfLastWord('hello world') == 5
    assert s.lengthOfLastWord('   hello world   ') == 5
    assert s.lengthOfLastWord('helloworld') == 10
    assert s.lengthOfLastWord('') == 0

