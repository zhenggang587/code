import random

class Solution:
    def __init__(self):
        self.unigram = {}
        self.bigram = {}

    def train(self, s):
        words = s.split(" ")
        for word in words:
            word = '^' + word + '$'
            for i in range(len(word)):
                c = word[i]
                if c not in self.unigram:
                    self.unigram[c] = 0
                self.unigram[c] += 1
                if i < len(word) - 1:
                    d = word[i + 1]
                    if c not in self.bigram:
                        self.bigram[c] = {}
                    if d not in self.bigram[c]:
                        self.bigram[c][d] = 0
                    self.bigram[c][d] += 1

        for c, bi in self.bigram.items():
            pre = 0
            for d, cnt in self.bigram[c].items():
                self.bigram[c][d] += pre
                pre = self.bigram[c][d]

    def generate(self):
        cur = '^' 
        ret = ''
        while cur != '$':
            k = random.randint(1, self.unigram[cur])
            bi = self.bigram[cur]
            for d, cnt in bi.items():
                if k <= cnt:
                    ret += d
                    cur = d
                    break
        return ret[:-1]


if __name__ == "__main__":
    s = Solution()
    
    s.train('ape apple ace')
    print s.generate()
    print s.generate()
    print s.generate()
