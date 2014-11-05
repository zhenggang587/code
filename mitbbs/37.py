
class Solution:
    def getSolution(self, A):
        count = [0]
        self.traverse(A, 0, 0, count)
        return count[0]

    def traverse(self, A, i, sum, count):
        if sum == 15:
            count[0] += 1
            return
        if i >= len(A):
            return

        for k in range(i, len(A)):
            self.traverse(A, k + 1, sum + A[k], count)

if __name__ == "__main__":
    s = Solution()
    
    assert s.getSolution([5, 5, 10, 2, 3]) == 4
    assert s.getSolution([1, 2, 3, 4, 5]) == 1
