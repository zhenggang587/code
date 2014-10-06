
class Solution:
    # @return a string
    def countAndSay(self, n):
        say = '1'
        for i in range(2, n + 1):
           say = self.count(say) 
        return say

    def count(self, say):
        cnt = 1
        base = say[0]
        index = 0
        ret = ''
        while index + 1 < len(say):
            if say[index + 1] != base:
                ret += str(cnt) + base
                base = say[index + 1]
                cnt = 1
            else:
                cnt += 1
            index += 1
        ret += str(cnt) + base
        return ret
        
if __name__ == "__main__":
    s = Solution()

    print s.countAndSay(10)
