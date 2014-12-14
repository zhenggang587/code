
INT_MAX = (1 << 31)

class Solution:
    def getSolution(self, A, B):
        n = len(A)
        left = A
        used = []
        i = 0
        while i < n:
            if i < n - 1 and B[i] in left:
                used.append(B[i])
                left.remove(B[i])
                i += 1
            else:
                while i >= 0:
                    greater = self.find(left, B[i])
                    if greater != INT_MAX:
                        used.append(greater)
                        left.remove(greater)
                        left.sort()
                        used.extend(left)
                        return used
                    else:
                        if not used:
                            return False
                        left.append(used.pop())
                        i -= 1

    def find(self, arr, num):
        ret = INT_MAX
        for a in arr:
            if a > num and a < ret:
                ret = a
        return ret

         

if __name__ == "__main__":
    s = Solution()

    assert s.getSolution([1, 2, 3, 4], [2, 4, 3, 0]) == [2, 4, 3, 1]
    assert s.getSolution([1, 3], [1, 3]) == [3, 1]
    assert s.getSolution([1, 1], [1, 3]) == False
