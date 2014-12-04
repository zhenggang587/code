
'''
sort word list A by char sequence in string s
for example
A: ['face', 'ball', 'apple', 'art', 'ah']
s: 'htarfbp'
result: ['ah', 'art', 'apple', 'face', 'ball']

'''

class Solution:
    def getSolution(self, A, s):
        self.s = s
        return sorted(A, self.cmp)

    def cmp(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i, j = 0, 0
        while i < m and j < n and word1[i] == word2[j]:
            i += 1
            j += 1
        if i >= m and j >= n:
            return 0
        elif i >= m:
            return 1
        elif j >= n:
            return -1

        index1 = self.s.index(word1[i])
        index2 = self.s.index(word2[j])
        if index1 != -1 and index1 < index2:
            return -1
        elif index2 != -1 and index2 < index1:
            return 1
        return 0
        

if __name__ == "__main__":
    s = Solution()

    print s.getSolution(['face', 'ball', 'apple', 'art', 'ah'], 'htarfbp')
