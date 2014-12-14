
# assume no parentheses 

class Formula:
    def __init__(self, s):
        self.s = s 

    def calculate(self):
        s = self.s
        priority = {'+': 0, '-': 0, '*': 1, '/': 1}
        numStack = []
        opStack = []
        token = ''
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                token += s[i]
            else:
                numStack.append(int(token))
                token = ''

                while opStack and priority[opStack[-1]] >= priority[s[i]]:
                    rightNum = numStack.pop()
                    leftNum = numStack.pop()
                    op = opStack.pop()
                    if op == '+':
                        res = leftNum + rightNum
                    elif op == '-':
                        res = leftNum - rightNum
                    elif op == '*':
                        res = leftNum * rightNum
                    else:
                        res = leftNum / rightNum
                    numStack.append(res)
                opStack.append(s[i])
        numStack.append(int(token))

        while opStack:
            op = opStack.pop()
            rightNum = numStack.pop()
            leftNum = numStack.pop()
            if op == '+':
                res = leftNum + rightNum
            elif op == '-':
                res = leftNum - rightNum
            elif op == '*':
                res = leftNum * rightNum
            else:
                res = leftNum / rightNum
            numStack.append(res)
        return numStack[0]


    def tostring(self):
        return self.s 

if __name__ == "__main__":
    s = Formula('3/6-1*4+11')
    
    print s.calculate()
