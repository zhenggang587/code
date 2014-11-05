
class Solution:
    def getSolution(self, A):
        x = 0
        for a in A:
            x ^= a

        for i in range(32):
            if x & (1 << i) != 0:
                break

        x, y = 0, 0
        for a in A:
            if a & (1 << i) == 0:
                x ^= a
            else:
                y ^= a

        return x, y

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 1, 2, 2, 3, 4])
