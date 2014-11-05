
class Solution:
    def getSolution(self, A, k):
        if k == 0:
            return None

        count = [0 for i in range(k)]
        for a in A:
            count[a % k] += 1

        if count[0] % 2 != 0:
            return False
        if k % 2 == 0 and count[k / 2] % 2 != 0:
            return False
        for i in range(1, k / 2 + 1):
            if count[i] != count[k - i]:
                return False
        return True
            

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 5, 3, 6], 3)
