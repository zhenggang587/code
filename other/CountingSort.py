
class Solution:
    # assume all positive number
    def countingSort(self, A):
        maxNum = max(A)
        arr = [0 for i in range(maxNum + 1)]
        for a in A:
            arr[a] += 1

        ret = []
        for i in range(len(arr)):
            ret.extend([i for j in range(arr[i])])
        return ret
        

if __name__ == "__main__":
    s = Solution()

    A = [3, 1, 4]
    print s.countingSort(A)
