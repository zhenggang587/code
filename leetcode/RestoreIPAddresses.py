
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        path = []
        paths = []
        self.traverse(s, 0, path, paths)

        return paths

    def traverse(self, s, index, path, paths):
        if index == len(s):
            if len(path) == 4:
                paths.append(".".join(path))
            return
        if index < len(s) and len(path) >= 4:
            return

        for offset in range(3):
            end = index + offset
            if end >= len(s):
                break
            part = int(s[index:end+1])
            if len(str(part)) != offset + 1: # such as 000
                break 
            if part > 255:
                break 

            path.append(str(part))
            self.traverse(s, end + 1, path, paths)
            path.pop()

if __name__ == "__main__":
    s = Solution()

    print s.restoreIpAddresses("00000")
