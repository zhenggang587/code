
# assume no parentheses 

class Formula:
    def __init__(self, s):
        self.s = s 

    def calculate(self):
        s = self.s
        start = end = 0
        numStack = []
        symbolStack = []
        while end < len(self.s):
            if s[end] in '+-*/':
                num = int(self.s[start:end])
                start = end + 1
                if not numStack:
                    numStack.append(num)
                if not symbolStack:
                    symbolStack.append(s[end])
                else:
                    if symbolStack[-1] in '+-' and s[end] in '*/':
                        numStack.append(num)
                    else:
                        lop = numStack.pop()
                        symbol = symbolStack.pop()
                        if symbol == '+':
                            val = lop + num
                        elif symbol == '-':
                            val = lop - num
                        elif symbol == '*':
                            val = lop * num
                        else:
                            val = lop / num
                        numStack.append(val)
                    symbolStack.append(s[end])
            end += 1

        num = int(self.s[start:end])
        numStack.append(num)
        while symbolStack:
            rop = numStack.pop()
            lop = numStack.pop()
            symbol = symbolStack.pop()
            if symbol == '+':
                val = lop + rop
            elif symbol == '-':
                val = lop - rop
            elif symbol == '*':
                val = lop * rop
            else:
                val = lop / rop
            numStack.append(val)
        return numStack[0]


    def tostring(self):
        return self.s 

if __name__ == "__main__":
    s = Formula('1+2*3')
    
    print s.calculate()
