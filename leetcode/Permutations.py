
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        paths = []

        self.traverse(num, 0, paths)
        return paths
        
    def traverse(self, num, index, paths):
        if index == len(num):
            paths.append(num[:])
            return

        for k in range(index, len(num)):
            num[k], num[index] = num[index], num[k]
            self.traverse(num, index + 1, paths)
            num[k], num[index] = num[index], num[k]
        
if __name__ == "__main__":
    s = Solution()

    print s.permute([1, 2, 3])
