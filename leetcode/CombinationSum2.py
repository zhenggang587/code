
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        cands = sorted(set(candidates))

        path = []
        paths = []
        self.traverse(cands, target, path, paths)
        return paths

    def traverse(self, candidates, target, path, paths):
        if target == 0:
            paths.append(path[:])
            return
        if target < 0:
            return

        for i in range(len(candidates)):
            path.append(candidates[i])
            self.traverse(candidates[i:], target - candidates[i], path, paths)
            path.pop()
        
if __name__ == "__main__":
    s = Solution()

    print s.combinationSum([2, 2], 4)
