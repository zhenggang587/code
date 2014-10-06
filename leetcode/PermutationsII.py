
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        paths = []

        self.traverse(num, 0, paths)
        return paths

    def isValid(self, num, i, j):
        for k in range(i, j):
            if num[k] == num[j]:
                return False
        return True
        
    def traverse(self, num, index, paths):
        if index == len(num):
            paths.append(num[:])
            return

        for k in range(index, len(num)):
            if not self.isValid(num, index, k):
                continue

            num[k], num[index] = num[index], num[k]
            self.traverse(num, index + 1, paths)
            num[k], num[index] = num[index], num[k]
        
if __name__ == "__main__":
    s = Solution()

    print s.permuteUnique([0,1,0,0,9])
