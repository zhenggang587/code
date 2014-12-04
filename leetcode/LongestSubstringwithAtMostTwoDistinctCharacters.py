
'''
Longest Substring with At Most Two Distinct Characters, return max length
'''
class Solution:
    def getSolution(self, s):
        indexMap = {}
        ret = 0
        start = end = 0
        n = len(s)
        while end < n:
            if s[end] not in indexMap and len(indexMap) == 2:
                minIndex = (1 << 31)
                minC = ''
                for c, index in indexMap.items():
                    if index < minIndex:
                        minIndex = index
                        minC = c
                del indexMap[minC]
                start = minIndex + 1
            else:
                ret = max(ret, end - start + 1)
            indexMap[s[end]] = end
            end += 1
        return ret


if __name__ == "__main__":
    s = Solution()

    print s.getSolution('abcccaaab')
    print s.getSolution('abcabcbb')
    print s.getSolution('bbb')
    print s.getSolution('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco')
    print s.getSolution('qopubjguxhxdipfzwswybgfylqvjzhar')
