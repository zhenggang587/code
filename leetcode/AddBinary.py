
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a_index = len(a) - 1
        b_index = len(b) - 1
        borrow = 0
        ret = []
        while a_index >= 0 and b_index >= 0:
           c = int(a[a_index]) + int(b[b_index]) + borrow
           ret.append(c % 2)
           borrow = c / 2
           a_index -= 1
           b_index -= 1

        while a_index >= 0:
            c = int(a[a_index]) + borrow
            ret.append(c % 2)
            borrow = c / 2
            a_index -= 1

        while b_index >= 0:
            c = int(b[b_index]) + borrow
            ret.append(c % 2)
            borrow = c / 2
            b_index -= 1
        if borrow:
            ret.append(borrow)

        ret_str = ""
        for i in range(len(ret) - 1, -1, -1):
            ret_str += str(ret[i])

        return ret_str

           
        
if __name__ == "__main__":
    s = Solution()

    print s.addBinary("111111111", "")
