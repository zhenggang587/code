
class Solution:
    def getSolution(self, strs):
        m = {}
        for i in range(len(strs)):
            words = [word.lower() for word in strs[i].split(" ") if word]
            key = " ".join(sorted(words))
            m[key] = (i, strs[i])

        return [val[1] for val in sorted(m.values())]


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(["apple Orange", "ORANGE apple", "APPLe oRange", "HI There", "THERE hI"])
