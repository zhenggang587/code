
class Solution:
    def gcd(self, a, b):
        if a > b:
            return self.gcd(b, a)

        if b % a == 0:
            return a
        return self.gcd(b % a, a)

if __name__ == "__main__":
    s = Solution()

    print s.gcd(20, 7)
