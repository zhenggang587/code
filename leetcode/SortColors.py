
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        zero_index = one_index = -1 
        l = len(A)
        for i in range(l):
            if A[i] == 0:
                if self.swap(A, i, zero_index + 1):
                    zero_index += 1
                    if one_index < zero_index:
                        one_index = zero_index
            if A[i] == 1:
                if self.swap(A, i, one_index + 1):
                    one_index += 1

    def swap(self, A, i, j):
        if i < len(A) and j < len(A):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            return True
        return False
                
        
if __name__ == "__main__":
    s = Solution()

    A = [2, 0, 1, 2, 2, 1, 0, 0, 0, 0]
    s.sortColors(A)
    print A

