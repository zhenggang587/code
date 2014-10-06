
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return ['']

        ret = []
        for i in range(n):
            left_res = self.generateParenthesis(i)
            right_res = self.generateParenthesis(n - 1 - i)
            for left_one in left_res:
                for right_one in right_res:
                    ret.append('(' + left_one + ')' + right_one)

        return ret

        
if __name__ == "__main__":
    s = Solution()

    print s.generateParenthesis(3)
