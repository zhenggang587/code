
class Solution:
    def getSolution(self, strs):
        strs.sort(self.compare)
        return strs

    def compare(self, s1, s2):
        parts1 = s1.split(".")
        parts2 = s2.split(".")

        if int(parts1[0]) > int(parts2[0]):
            return 1
        elif int(parts1[0]) < int(parts2[0]):
            return -1
        else:
            if len(parts1) == 1 and len(parts2) == 1:
                return 0
            elif len(parts1) == 1:
                return -1
            elif len(parts2) == 1:
                return 1
            elif int(parts1[1]) > int(parts2[1]):
                return 1
            elif int(parts1[1]) < int(parts2[1]):
                return -1
            return 0



if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(['0.25', '0.15'])
