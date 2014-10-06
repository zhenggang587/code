
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a_index = len(a) - 1
        b_index = len(b) - 1
        borrow = 0
        ret = []
        while a_index >= 0 or b_index >= 0:
            if a_index >= 0:
                borrow += int(a[a_index])
                a_index -= 1
            if b_index >= 0:
                borrow += int(b[b_index])
                b_index -= 1
            ret.append(borrow % 2)
            borrow /= 2
        if borrow:
            ret.append(borrow)

        ret_str = ""
        for i in range(len(ret) - 1, -1, -1):
            ret_str += str(ret[i])

        return ret_str

           
        
if __name__ == "__main__":
    s = Solution()

    print s.addBinary("111111111", "1")
