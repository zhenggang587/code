
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return []
        ret = []
        borrow = 0
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            c = digits[i] + borrow
            ret.append(c % 10)
            borrow = c / 10
        if borrow:
            ret.append(borrow)

        return ret[::-1]
        
if __name__ == "__main__":
    s = Solution()

    print s.plusOne([9, 9])

