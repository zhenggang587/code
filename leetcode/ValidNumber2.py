
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        INVALID, SPACE, SIGN, DIGIT, DOT, EXPONET = 0, 1, 2, 3, 4, 5
        transtable = [
        [-1, 0, 3, 1, 2, -1],      # no input or only space
        [-1, 8, -1, 1, 4, 5],      # after input num
        [-1, -1, -1, 4, -1, -1],   # only dot, no num before
        [-1, -1, -1, 1, 2, -1],    # after input sign
        [-1, 8, -1, 4, -1, 5],     # has num and dot after num
        [-1, -1, 6, 7, -1, -1],    # after input e or E 
        [-1, -1, -1, 7, -1, -1],   # sign after e
        [-1, 8, -1, 7, -1, -1],    # num after e
        [-1, 8, -1, -1, -1, -1], # all valid, and then input space
        ]

        state = 0
        for c in s:
            a = INVALID
            if c == ' ':
                a = SPACE
            elif c == '+' or c == '-':
                a = SIGN
            elif c.isdigit():
                a = DIGIT
            elif c == '.':
                a = DOT
            elif c == 'e' or c == 'E':
                a = EXPONET
            state = transtable[state][a]
            if state == -1:
                return False
        return state in (1, 4, 7, 8)
        
if __name__ == "__main__":
    s = Solution()

    assert s.isNumber("+") == False
    assert s.isNumber("") == False 
    assert s.isNumber(".1") == True
    assert s.isNumber(".") == False
    assert s.isNumber("0") == True
    assert s.isNumber("3") == True
    assert s.isNumber(" 0.1 ") == True
    assert s.isNumber("abc") == False
    assert s.isNumber("1 abc") == False
    assert s.isNumber("2e10") == True
    assert s.isNumber("-2e10") == True
    assert s.isNumber("+2e10") == True
    assert s.isNumber("+002e10") == True
    assert s.isNumber("01") == True
    assert s.isNumber("3.") == True
    assert s.isNumber(".3.") == False
    assert s.isNumber("0e ") == False
    assert s.isNumber("46.e3") == True
