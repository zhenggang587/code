
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        cand = sorted(candidates)

        path = []
        paths = []
        self.traverse(cand, 0, target, path, paths)
        return paths

    def traverse(self, candidates, index, target, path, paths):
        if target == 0:
            paths.append(path[:])
            return 
        if index >= len(candidates):
            return
        if candidates[index] > target:
            return

        for i in range(index, len(candidates)):
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.traverse(candidates, i + 1, target - candidates[i], path, paths)
            path.pop() 
        
        
if __name__ == "__main__":
    s = Solution()

    print s.combinationSum2([10,1,2,7,6,1,5], 8)
    print s.combinationSum2([1], 1)
