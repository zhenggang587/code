
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        match = [-1 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                match[i] = stack.pop()

        max_len = 0
        sub_len = 0
        index = len(s) - 1
        while index >= 0:
            if match[index] < 0:
                if sub_len > max_len:
                    max_len = sub_len
                sub_len = 0
            else:
                sub_len += index - match[index] + 1
                index = match[index]
            index -= 1
        if sub_len > max_len:
            max_len = sub_len

        return max_len
        
        
if __name__ == "__main__":
    s = Solution()

    assert s.longestValidParentheses('(()') == 2
    assert s.longestValidParentheses(')()())') == 4
    assert s.longestValidParentheses('(()())') == 6
    assert s.longestValidParentheses('()(()') == 2
