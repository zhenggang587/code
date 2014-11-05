
class Solution:
    def getSolution(self, A, B):
        for i in range(len(B)):
            if B[i] in A:
                A.remove(B[i])
            else:
                bigger = self.findBigger(A, B[i])
                while bigger == (1 << 31) and i > 0:
                    i -= 1
                    A.add(B[i])
                    bigger = self.findBigger(A, B[i])
                if bigger == (1 << 31):
                    return False
                else:
                    ret = B[:i]
                    ret.append(bigger)
                    A.remove(bigger)
                    ret.extend(sorted(A))
                    return ret
        return False

    def findBigger(self, A, num):
        ret = (1 << 31)
        for a in A:
            if a > num and a < ret:
                ret = a
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([4, 0, 6, 0], [5, 1, 3, 2])
