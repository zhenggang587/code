
# nlog(n)log(m)
# nlogn是指先选定一个数k，再二分搜索(m-k)，如果找到了则这两个成一组，如果找不到则表示m不可能是最大值，如果找的数(假设为l)+k小于m，则用m - k -l继续去找，尽量把这一组填满
# 第一个数k也是找最大的

class Solution:
    def getSolution(self, A):

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
