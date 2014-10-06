
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

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
