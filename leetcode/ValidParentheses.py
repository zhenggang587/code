
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        map = {'[': ']', '{': '}', '(': ')'}
        for c in s:
            if not stack:
                if c not in map:
                    return False
                stack.append(c)
                continue

            
            if c == map[stack[-1]]:
                stack.pop()
            elif c in map:
                stack.append(c)
            else:
                return False

        return not stack
        
if __name__ == "__main__":
    s = Solution()

    print s.isValid('[]')
