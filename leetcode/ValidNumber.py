
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
            else:
                break
        if index == len(s):
            return False

        if s[index] == '+' or s[index] == '-':
            index += 1
            if index >= len(s):
                return False

        has_dot = False
        if s[index] == '.':
            has_dot = True
            if index + 1 < len(s):
                if s[index + 1]  >= '0' and s[index + 1] <= '9':
                    index += 1
                else:
                    return False
            else:
                return False
        elif not (s[index] >= '0' and s[index] <= '9'):
            return False
        else:
            index += 1

        while index < len(s):
            if s[index] >= '0' and s[index] <= '9':
                index += 1
            else:
                break
        if index >= len(s):
            return True
        if s[index] == '.':
            if has_dot:
                return False
            index += 1
            while index < len(s):
                if s[index] >= '0' and s[index] <= '9':
                    index += 1
                else:
                    break
        if index >= len(s):
            return True
        if s[index] == 'e':
            if index + 1 >= len(s):
                return False
            if s[index + 1] == '+' or s[index + 1] == '-':
                index += 1
            index += 1
            base_index = index
            while index < len(s):
                if s[index] >= '0' and s[index] <= '9':
                    index += 1
                else:
                    break
            if base_index == index:
                return False

        while index < len(s):
            if s[index] == ' ':
                index += 1
            else:
                return False
        return True
        
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
