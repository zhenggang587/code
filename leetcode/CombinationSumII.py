
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

        end = index + 1
        while end < len(candidates):
            if candidates[end] != candidates[index]:
                break
            end += 1

        length = end - index
        for i in range(length + 1):
            for j in range(i):
                path.append(candidates[index])
            self.traverse(candidates, end, target - i * candidates[index], path, paths)
            for j in range(i):
                path.pop() 
        
        
if __name__ == "__main__":
    s = Solution()

    print s.combinationSum2([10,1,2,7,6,1,5], 8)
    print s.combinationSum2([1], 1)
