
class Solution:
    def getSolution(self, A, B):
        ret = ''
        ia = ib = 0
        ja = jb = 0
        while ia < len(A) and ib < len(B):
            ret += A[ia][ja]
            ja += 1
            if ia < len(A) and ja == len(A[ia]):
                ia += 1
                ja = 0
            if ia >= len(A):
                return ret

            ret += B[ib][jb]
            jb += 1
            if ib < len(B) and jb == len(B[ib]):
                ib += 1
                jb = 0
            if ib >= len(B):
                return ret
        return ret

                

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(['abc', 'mn'], ['pa', 'd'])
