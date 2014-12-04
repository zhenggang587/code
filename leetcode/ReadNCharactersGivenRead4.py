
class Solution:
    def __init__(self, s):
        self.s = s
        self.offset = 0
        
    def _read4(self):
        tmp = self.s[self.offset:self.offset + 4]
        self.offset += 4
        return tmp

    def readN(self, n):
        self.offset = 0
        ret = ''
        left = n
        while left > 0:
            tmp = self._read4()
            if not tmp:
                break
            ret += tmp[:left]
            left -= len(tmp) 
        return ret


if __name__ == "__main__":
    s = Solution('54312')

    assert s.readN(0) == ''
    assert s.readN(3) == '543'
    assert s.readN(4) == '5431'
    assert s.readN(30) == '54312'
        
