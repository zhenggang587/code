
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        num_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}
        path = ''
        paths = []
        self.traverse(digits, 0, num_map, path, paths)
        return paths

    def traverse(self, digits, index, num_map, path, paths):
        if index == len(digits):
            paths.append(path)
            return
        if digits[index] not in num_map:
            return

        for c in num_map[digits[index]]:
            self.traverse(digits, index + 1, num_map, path + c, paths)
        

if __name__ == "__main__":
    s = Solution()

    print s.letterCombinations('2')
