
class Solution:
    def getSolution(self, s):
        INVALID, CHAR, SLASH, BACKSLASH, STAR, N = 0, 1, 2, 3, 4, 5
        transtable = [
        [-1, 0, 1, 0, 0, 0],  # no input or input char
        [-1, 0, 2, 0, 3, 0], # one slash
        [-1, 2, 2, 4, 2, 2], # two slash
        [-1, 3, 3, 3, 5, 3], # one slash and star
        [-1, 4, 4, 4, 4, 6], # two slash and a backslash
        [-1, 5, 7, 5, 5, 5], # a slash and start and a slash
        [-1, 0, 1, 0, 0, 0], # two slash and newline
        [-1, 0, 1, 0, 0, 0], # /* */
        ]
        state = 0
        ret = ''
        stash = ''
        for c in s:
            a = INVALID
            if c == '/':
                a = SLASH
            elif c == '\\':
                a = BACKSLASH
            elif c == '*':
                a = STAR
            elif c == 'n':
                a = N
            else:
                a = CHAR

            state = transtable[state][a]
            if state == -1:
                break
            elif state == 0:
                ret += stash + c
                stash = ''
            elif state in [1, 3, 5]:
                stash += c
            elif state in [2, 4, 7]:
                stash = ''
            elif state == 6:
                stash = ''
                ret += '\\n'

        return ret + stash
                

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('abc//xyz\\nwwe*/*sdfsd/*sdfda*/sd*/cvcd')
