
class Solution:
    def getSolution(self, A):
        if not A:
            return False

        a, b = 1, 1
        while a < A[0]:
            a = a + b
            b = a + b
            if b >= A[0]:
                break
        if a != A[0] and b != A[0]:
            return False
        if a == A[0]:
            tmp = b - a
            b = a
            a = tmp

        index = 0
        while index < len(A):
            if b != A[index]:
                return False
            a = a + b
            index += 1
            if index < len(A) and A[index] != a:
                return False
            b = a + b
            index += 1

        return True


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([2, 3, 5, 8, 13, 20])
