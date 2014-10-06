
class Solution:
    def getSolution(self, s, num):
        index = 0
        word = ''
        while index < len(s):
            if s[index] != ' ':
                word += s[index]
            else:
                wn = int(word)
                if wn == num:
                    return True
                elif wn > num:
                    return False
                word = ''
            index += 1
        if word and int(word) == num:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('1 23 45 1000', 10000)
