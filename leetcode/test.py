class Solution:
    def decimal(self, num1, num2):
        if num1 == 0:
            return 0
        if num2 == 0:
            raise Exception('divide zero')

        sign = 1
        if num1 < 0:
            num1 = -num1
            sign = -sign
        if num2 < 0:
            num2 = -num2
            sign = -sign

        ret = ''
        if sign < 0:
            ret += '-'

        ret += str(num1 / num2) + '.'
        num1 %= num2
        remain = {}
        digit = ''
        index = 0
        cycle_start = -1
        while num1:
            if num1 not in remain:
                remain[num1] = index
            else:
                cycle_start = remain[num1]
                break
            num1 *= 10
            digit += str(num1 / num2)
            num1 %= num2
            index += 1


        if cycle_start >= 0:
            ret += digit[:cycle_start] + '(' + digit[cycle_start:] + ')'
        else:
            ret += digit + '(0)'
        return ret




                
            
            
        

if __name__ == "__main__":
    s = Solution()
     
    print s.decimal(1, 0)
    print s.decimal(2, 4)
    print s.decimal(22, -7)
