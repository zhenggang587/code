
# 先用dp算出每个点top, bottom, left, right4个方向能到达的最远距离 O(n^2)
# 再对每条对角线 O(n)
#*  对每个点按min(left, top)排序 O(nlog(n)), 比如(0, 0)点可从(3, 3)到达, (1, 1)点可从(4, 4)到达
#*  再从对角线左上角往下走，记一个当前点能到达的最远点，然后更新距离 O(n)

class Solution:
    def getSolution(self, ):

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
