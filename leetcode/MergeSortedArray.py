
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        a_index = m - 1
        b_index = n - 1
        c_index = m + n - 1
        while a_index >= 0 and b_index >= 0:
            if A[a_index] > B[b_index]:
                A[c_index] = A[a_index]
                a_index -= 1
            else:
                A[c_index] = B[b_index]
                b_index -= 1
            c_index -= 1
        while a_index >= 0:
            A[c_index] = A[a_index]
            a_index -= 1
            c_index -= 1
        while b_index >= 0:
            A[c_index] = B[b_index]
            b_index -= 1
            c_index -= 1

        
if __name__ == "__main__":
    s = Solution()

    A = [1, 3, 5, 0, 0]
    B = [2, 4]
    s.merge(A, 3, B, 2)
    print A
