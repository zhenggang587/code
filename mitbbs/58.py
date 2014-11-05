
class Solution:
    def getSolution(self, arr):
        n = len(arr) / 2
        i = 0
        k = 1
        while i < n:
            tmp = arr[n + i]
            for j in range(n + i, k, -1):
                arr[j] = arr[j - 1]
            arr[k] = tmp
            k += 2
            i += 1
        return arr

    def getIndex(self, arr, index):
        n = len(arr) / 2
        return (index % 2) * n + index / 2

    def getSolution1(self, arr):
        for index in range(len(arr)):
            swapIndex = self.getIndex(arr, index)
            while swapIndex < index:
                swapIndex = self.getIndex(arr, swapIndex)

            arr[index], arr[swapIndex] = arr[swapIndex], arr[index]
        return arr

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
    print s.getSolution1([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
