
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        red = 0
        blue = len(A) - 1
        i = 0
        while i <= blue:
            if A[i] == 0:
                A[i], A[red] = A[red], A[i]
                i += 1
                red += 1
            elif A[i] == 2:
                A[i], A[blue] = A[blue], A[i]
                blue -= 1
            else:
                i += 1


        
if __name__ == "__main__":
    s = Solution()

    A = [2, 0, 1, 2, 2, 1, 0, 0, 0, 0]
    s.sortColors(A)
    print A

