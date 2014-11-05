
class Solution:
    def getSolution(self, num):
        m = {}
        index = 0
        while num:
            digit = num % 10
            if digit not in m:
                m[digit] = []
            m[digit].append(index)
            num /= 10
            index += 1

        ret = {}
        for digit, indexs in m.items():
            if len(indexs) > 1:
                ret[digit] = indexs
        return ret
            

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(10010)
