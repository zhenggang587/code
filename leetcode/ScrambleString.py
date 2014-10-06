import time

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if not s1:
            return True

        state = [[[True if (k == 1 and s1[i] == s2[j]) or k == 0 else False for k in range(len(s1) + 1)] for j in range(len(s1))] for i in range(len(s1))]
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s1) - 1, -1, -1):
                l = len(s1) + 1 - max(i, j)
                for k in range(1, l):
                    for m in range(1, k):
                        if (state[i][j][m] and state[i + m][j + m][k - m]) or (state[i][j + k - m][m] and state[i + m][j][k - m]):
                            state[i][j][k] = True
                            break   

        return state[0][0][len(s1)] 
        
if __name__ == "__main__":
    s = Solution()

    assert s.isScramble('great', 'rtgae') == False
    assert s.isScramble('great', 'rgtae') == True
    assert s.isScramble('ba', 'ab') == True
    now = time.time()
    assert s.isScramble('abcdefghijklmn', 'efghijklmncadb') == False
    print time.time() - now
