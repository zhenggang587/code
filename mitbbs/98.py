
class Solution:
    def getSolution(self, arr, key):
        if not arr:
            return False

        l = 0
        r = 1
        while True:
            try:
                if arr[l] == key:
                    return True
                elif arr[l] < key:
                    l = r
                    r *= 2
                else:
                    break
            except IndexError:
                break

        r = l
        l = r / 2
        while l <= r:
            m = l + (r - l) / 2
            try:
                if arr[m] == key:
                    return True
                elif arr[m] < key:
                    l = m + 1
                else:
                    r = m - 1
            except IndexError:
                r = m - 1
        return False


if __name__ == "__main__":
    s = Solution()
    
    assert s.getSolution([1, 2, 3, 5, 10], 10) == True
    assert s.getSolution([1, 2, 3, 5, 10], 5) == True
    assert s.getSolution([1, 2, 3, 5, 10], -1) == False
    assert s.getSolution([1, 2, 3, 5, 10], 3) == True
    assert s.getSolution([1, 2, 3, 5, 10], 1) == True
