'''
if a[i] == b[j]:
    if s[i - 1][j - 1] == True
        s[i][j] = True
if s[i - 1][j]:
    s[i][j] = True


s[3][3] = s[2][2]

s[3][2] = s[2][2]
'''

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        state = [[1 if j == 0 else 0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]
        for i in range(1, len(S) + 1):
            for j in range(1, len(T) + 1):
                if S[i - 1] == T[j - 1] and state[i - 1][j - 1]:
                    state[i][j] = state[i - 1][j - 1]
                if state[i - 1][j]:
                    state[i][j] += state[i - 1][j]

        return state[len(S)][len(T)]
        
if __name__ == "__main__":
    s = Solution()

    print s.numDistinct("", "")

