
# WA
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        n = len(words)
        index = 0
        ans = []
        while index < n:
            total = 0
            j = 0
            for j in range(index, n):
                total += len(words[j])
                if total >= L:
                    break
            
            l = L - (total - len(words[j]))
            j -= 1
            if j < 0:
                break
            spaces = [l / (j - index) for k in range(j - index)]
            for k in range(l % (j - index)):
                spaces[k] += 1
            s = ''
            for i in range(j - index):
                s += words[index + i] + ' ' * spaces[i]
            s += words[j]

            ans.append(s)

            index = j + 1

        if len(ans) > 0:
            ans[-1] = ''.join(ans[-1].split())
        return ans

if __name__ == "__main__":
    s = Solution()

    print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)

