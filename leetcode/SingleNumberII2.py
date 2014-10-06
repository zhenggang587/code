
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A): 
        one, two, three = 0, 0, 0
        for a in A:
            two |= (one & a)
            one ^= a
            three = ~(two & one)
            one &= three
            two &= three

        return one


if __name__ == "__main__":
    s = Solution()

    assert s.singleNumber([1, 1, 1, 3]) == 3
