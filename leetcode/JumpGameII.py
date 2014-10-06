
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) == 1:
            return 0

        queue = []
        queue.append((A[0], 1))
        for i in range(1, len(A)):
            index, cnt  = queue[0]
            if index >= len(A) - 1:
                return cnt
            end_index, end_cnt = queue[len(queue) - 1]
            if i + A[i] > end_index:
                queue.append((i + A[i], cnt + 1))
            if i == index:
                queue.pop(0)

        end_index, end_cnt = queue[len(queue) - 1]
        if end_index >= len(A) - 1:
            return end_cnt

        return -1
        
        
if __name__ == "__main__":
    s = Solution()

    print s.jump([2,3,1,1,4])
    print s.jump([1, 1, 1, 1])
    print s.jump([1])
