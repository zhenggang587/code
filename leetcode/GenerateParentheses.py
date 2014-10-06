
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return self.traverse(0, 2 * n - 1)

    def traverse(self, left, right):
        if left > right:
            return ['']

        ret = []
        for i in range(left + 1, right + 1, 2):
            left_res = self.traverse(left + 1, i - 1)
            right_res = self.traverse(i + 1, right)
            for left_one in left_res:
                for right_one in right_res:
                    ret.append('(' + left_one + ')' + right_one)

        return ret

        
if __name__ == "__main__":
    s = Solution()

    print s.generateParenthesis(3)
