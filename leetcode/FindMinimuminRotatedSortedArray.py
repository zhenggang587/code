
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num:
            return -1

        l = 0
        r = len(num) - 1
        while l <= r:
            m = l + (r - l) / 2
            if num[m] == num[r]:
                return num[m]
            elif num[m] > num[r]:
                l = m + 1
            else:
                r = m


if __name__ == "__main__":
    s = Solution()

    print s.findMin([1, 2])
