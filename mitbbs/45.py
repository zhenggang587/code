
class Solution:
    def getSolution(self, A, B):
        if len(B) > len(A):
            return None

        tMap = {}
        tSet = set()
        for c in B:
            if c not in tMap:
                tMap[c] = 0
                tSet.add(c)
            tMap[c] += 1

        m = len(A)
        n = len(B)
        for i in range(m):
            c = A[i]
            if c in tSet:
                if c in tMap:
                    tMap[c] -= 1
                    if tMap[c] == 0:
                        del tMap[c]
                else:
                    tMap[c] = -1
            if i >= n and A[i-n] in tSet:
                c = A[i-n]
                if c in tMap:
                    tMap[c] += 1
                    if tMap[c] == 0:
                        del tMap[c]
                else:
                    tMap[c] = 1

            if not tMap:
                return A[i-n+1:i+1]
        return None 


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('abcdbcsdaqdbahs', 'scdcb')
