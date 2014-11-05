
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num:
            return -1
        n = len(num)
        l = 0
        r = n - 1
        while l < r:
            if r - l <= 1:
                return min(num[l], num[r])
            m = l + (r - l) / 2
            if num[m] == num[r]:
                return num[m]
            elif num[m] > num[r]:
                l = m
            else:
                r = m
        return num[l]


if __name__ == "__main__":
    s = Solution()

    print s.findMin([1, 2])
