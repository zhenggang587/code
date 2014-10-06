
class Solution:
    def getPrime(self, n):
        b = [0 for i in range(n + 1)]

        for i in range(2, n + 1):
            if not b[i]:
                for j in range(2 * i, n + 1, i):
                    b[j] = 1

        ret = []
        for i in range(1, n + 1):
            if not b[i]:
                ret.append(i)
        return ret

            


if __name__ == "__main__":
    s = Solution()

    print s.getPrime(20)
