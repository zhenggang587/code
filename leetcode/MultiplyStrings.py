

class Solution:
        
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        ret = [0 for i in range(len(num1) + len(num2))]

        for i in range(len(num1)):
            for j in range(len(num2)):
                k = i + j
                a = num1[len(num1) - 1 - i]
                b = num2[len(num2) - 1 - j]
                ret[k] += int(a) * int(b)
                if ret[k] >= 10:
                    ret[k + 1] += ret[k] / 10
                    ret[k] %= 10
                
        ret_str = ''
        for k in range(len(ret)):
            ret_str = str(ret[k]) + ret_str

        for k in range(len(ret_str)):
            if ret_str[k] != '0':
                break
                        
        print ret_str, k
        return ret_str[k:]


if __name__ == "__main__":
    s = Solution()  
    print s.multiply('999999', '9999999999999999999999')
    print s.multiply('1000000', '20000000000000000000000')
    print s.multiply('0', '20000000000000000000000')
    print s.multiply('1', '2')
