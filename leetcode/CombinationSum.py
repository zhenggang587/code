
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        cands = sorted(candidates)

        path = []
        paths = []
        self.traverse(cands, 0, target, path, paths)
        return paths

    def traverse(self, candidates, index, target, path, paths):
        if target == 0:
            if path not in paths:
                paths.append(path[:])
            return
        if index >= len(candidates):
            return
        if target < candidates[index]:
            return

        l = target / candidates[index]
        for i in range(l + 1):
            for j in range(i):
                path.append(candidates[index])
            self.traverse(candidates, index + 1, target - i * candidates[index], path, paths)
            for j in range(i):
                path.pop()
        
if __name__ == "__main__":
    s = Solution()

    print s.combinationSum([], 8)
