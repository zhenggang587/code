
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        match = [0 for i in range(len(s))]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                left = stack.pop()
                match[i] = i - left + 1
                if left > 0:
                    match[i] += match[left - 1]
                max_len = max(max_len, match[i]) 

        return max_len
        
        
if __name__ == "__main__":
    s = Solution()

    assert s.longestValidParentheses('(()') == 2
    assert s.longestValidParentheses(')()())') == 4
    assert s.longestValidParentheses('(()())') == 6
    assert s.longestValidParentheses('()(()') == 2
