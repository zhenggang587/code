
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in '+-*/':
                right_op = int(stack.pop())
                left_op = int(stack.pop())
                if token == '+':
                    stack.append(left_op + right_op)
                elif token == '-':
                    stack.append(left_op - right_op)
                elif token == '*':
                    stack.append(left_op * right_op)
                else:
                    res = left_op / right_op
                    if left_op * right_op < 0 and res * right_op != left_op:
                        res += 1
                    stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()
                
        
     
if __name__ == "__main__":
    s = Solution()

    print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    #assert s.evalRPN(["2", "1", "+", "3", "*"])==9
    #assert s.evalRPN(["4", "13", "5", "/", "+"])==6
