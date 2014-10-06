
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s[::-1]
        tokens = [token for token in s.split(" ") if len(token) > 0]       
        for i in range(len(tokens)):
            tokens[i] = tokens[i][::-1]

        return " ".join(tokens)

     
if __name__ == "__main__":
    s = Solution()

    print s.reverseWords('   ')
