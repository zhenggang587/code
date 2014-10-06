
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        counter = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in counter:
                counter[key] = []
            counter[key].append(s)

        ret = []
        for vals in counter.values():
            if len(vals) > 1:
                ret.extend(vals)
        return ret

       
if __name__ == "__main__":
    s = Solution()

    print s.anagrams(['eat', 'tea', 'and']) 
