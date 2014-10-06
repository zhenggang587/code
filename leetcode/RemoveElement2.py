
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        pos = 0
        for a in A:
            if a != elem:
                A[pos] = a
                pos += 1

        return pos

if __name__ == "__main__":
    s = Solution()

    assert s.removeElement([2], 2) == 0
    assert s.removeElement([2, 2, 2], 2) == 0
    assert s.removeElement([1, 1, 2], 2) == 2
    assert s.removeElement([1, 1, 1], 2) == 3
