
class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) <= 0 or len(T) <= 0:
            return ''

        target_map = {}
        current_map = {}
        for c in T:
            if c not in target_map:
                target_map[c] = 0
                current_map[c] = 0
            target_map[c] += 1
            
        min_start = -1
        min_end = len(S)
        start = end = 0
        count = 0
        while end < len(S):
            c = S[end]
            if c in target_map:
                current_map[c] += 1
                if current_map[c] <= target_map[c]:
                    count += 1
                if count == len(T):
                    while start <= end:
                        c = S[start]
                        if c not in target_map or current_map[c] > target_map[c]:
                            if c in target_map and current_map[c] > target_map[c]:
                                current_map[c] -= 1
                            start += 1
                            c = S[start]
                        else:
                            break
                    if end - start < min_end - min_start:
                        min_end = end
                        min_start = start
            end += 1

        if min_start == -1:
            return ''
        return S[min_start:min_end + 1]


if __name__ == "__main__":
    s = Solution()
    print s.minWindow("ab", "b")
    print s.minWindow("a", "a")
    print s.minWindow("aa", "aa")
    print s.minWindow("aaa", "aa")
    print s.minWindow("aa", "aaa")
    print s.minWindow("ADOBECODEBANC", "BANC")
