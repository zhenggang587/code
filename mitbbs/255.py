
class Solution:
    def getSolution(self, strs):
        self.partition(strs, 0, len(strs) - 1)
        return strs

    def partition(self, strs, l, r):
        if l >= r:
            return

        x = strs[l]
        i = l
        j = r
        while i < j:
            while i < j and self.compare(strs[j], x) >= 0:
                j -= 1
            strs[i] = strs[j]
            while i < j and self.compare(strs[i], x) <= 0:
                i += 1
            strs[j] = strs[i]
        strs[i] = x

        self.partition(strs, l, i - 1)
        self.partition(strs, i + 1, r)

    def compare(self, s1, s2):
        parts1 = s1.split(".")
        parts2 = s2.split(".")

        if int(parts1[0]) > int(parts2[0]):
            return 1
        elif int(parts1[0]) < int(parts2[0]):
            return -1
        else:
            if int(parts1[1]) > int(parts2[1]):
                return 1
            elif int(parts1[1]) < int(parts2[1]):
                return -1
            return 0



if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(['0.25', '0.15'])
