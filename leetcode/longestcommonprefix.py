INT_MAX = 1 << 31 - 1

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        min_str = ''
        min_len = INT_MAX 
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
                min_str = str

        if min_len == 0:
            return ''

        for str in strs:
            for i in range(len(min_str)):
                if str[i] != min_str[i]:
                    if i == 0:
                        return ''
                    min_str = min_str[:i]
                    break

        return min_str


if __name__ == "__main__":
    s = Solution()
    print s.longestCommonPrefix(["flower","flow","flight"])
