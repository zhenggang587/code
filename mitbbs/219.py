
# assume no duplicate element
# ask interviewer each array can select how many elements
# assume only one

class Solution:
    def getSolution(self, matrix):
        paths = []
        self.traverse(matrix, 0, [], paths)
        return paths
    
    def traverse(self, matrix, index, path, paths):
        if index == len(matrix):
            paths.append(path[:])
            return

        for e in matrix[index]:
            path.append(e)
            self.traverse(matrix, index + 1, path, paths)
            path.pop()
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([['a', 'b'], [3, 4, 5], [True, False]])
