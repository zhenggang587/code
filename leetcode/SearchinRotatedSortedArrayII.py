
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        for a in A:
            if target == a:
                return True

        return False
        
if __name__ == "__main__":
    s = Solution()

    assert s.search([2, 2, 2], -1) == False
    assert s.search([2, 2, 2], 2) == True
