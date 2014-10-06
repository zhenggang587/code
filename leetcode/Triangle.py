
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return 0
        INT_MAX = (1 << 31) - 1
        path = [INT_MAX for i in range(len(triangle))]

        path[0] = triangle[0][0]
        for row_index in range(1, len(triangle)):
            for col_index in range(row_index, -1, -1):
                if col_index > 0 and path[col_index - 1] < path[col_index]:
                    path[col_index] = path[col_index - 1]
                path[col_index] += triangle[row_index][col_index]
                
        ret = INT_MAX
        for p in path:
            if p < ret:
                ret = p
        return ret
            
        
if __name__ == "__main__":
    s = Solution()

    assert s.minimumTotal([
    [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]) == 11
