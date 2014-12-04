
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        hit_map = {}
        start = end = 0
        max_len = 0
        while end < len(s):
            c = s[end]
            if c not in hit_map or hit_map[c] < start:
                hit_map[c] = end
            else:
                if end - start > max_len:
                    max_len = end - start
                start = hit_map[c] + 1
                hit_map[c] = end
            end += 1
        if end - start > max_len:
            max_len = end - start

        return max_len


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring('abcabcbb')
    print s.lengthOfLongestSubstring('bbb')
    print s.lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco')
    print s.lengthOfLongestSubstring('qopubjguxhxdipfzwswybgfylqvjzhar')
