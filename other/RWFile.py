
class Solution:
    def ReadFile(self, name):
        with open(name, 'r') as handle:
            for line in handle:
                self.WriteFile('file', line)

    def WriteFile(self, name, line):
        with open(name, 'a') as handle:
            handle.writelines(line)

if __name__ == "__main__":
    s = Solution()

    s.ReadFile('RWFile.py')
