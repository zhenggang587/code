

class Solution:
    def trap(self, A): 
        if not A:
            return 0
        stack = [0]
        ret = 0 
        for i in range(1, len(A)):
            while stack:
                if A[stack[-1]] >= A[i]:
                    break
                j = stack.pop()
                if stack:
                    ret += (min(A[i], A[stack[-1]]) - A[j]) * (i - stack[-1] - 1)
            stack.append(i)
        return ret





if __name__ == "__main__":
    s = Solution()
    
    print s.trap([5, 2, 1, 2])
