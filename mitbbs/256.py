
# assume no duplicate word in the sentence
class Solution:
    def getSolution(self, strs):
        invertedMap = {}
        n = len(strs)
        for i in range(n):
            words = [word for word in strs[i].split(" ") if word]
            for word in words:
                if word not in invertedMap:
                    invertedMap[word] = []
                invertedMap[word].append(i)

        pairMap = {}
        for word, docs in invertedMap.items():
            if len(docs) < 2:
                continue
            for i in docs:
                for j in docs:
                    if i == j:
                        continue
                    if (i, j) not in pairMap:
                        pairMap[(i, j)] = 0
                    pairMap[(i, j)] += 1

        return max(pairMap.values())

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(["This is a good day", "This is a bad day", "That was good day"])
