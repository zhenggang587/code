
# hashmap, open address, (m, n) is in val

class Solution:
    def __init__(self, row, max_col):
        self.row = row
        self.arr = [None for i in range(row * max_col)]

    def get(self, m, n):
        return self.arr[n * self.row + m]

    def set(self, m, n, val):
        self.arr[n * self.row + m] = val

if __name__ == "__main__":
    s = Solution(3, 3)
    
    print s.get(1, 1)
    s.set(1, 1, 5)
    print s.get(1, 1)
