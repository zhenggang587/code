
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num) - 2, -1 , -1):
            if num[i] < num[i + 1]:
                self.findNext(num, i)
                return num

        self.revert(num, 0, len(num) - 1)
        return num

    def findNext(self, num, i):
        for j in range(len(num) - 1, i, -1):
            if num[j] > num[i]:
                num[i], num[j] = num[j], num[i]
                self.revert(num, i + 1, len(num) - 1)
                break

    def revert(self, num, left, right):
        while left < right:
            num[left], num[right] = num[right], num[left]
            left += 1
            right -= 1
      
if __name__ == "__main__":
    s = Solution()

    assert s.nextPermutation([1, 3, 2]) == [2, 1, 3]
    assert s.nextPermutation([1, 2, 3]) == [1, 3, 2]
    assert s.nextPermutation([3, 2, 1]) == [1, 2, 3]
    assert s.nextPermutation([1, 1, 5]) == [1, 5, 1]
