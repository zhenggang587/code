
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        counter = {}
        for s in strs:
            key = [0 for i in range(26)]
            for c in s:
                key[ord(c) - 97] += 1
            str_key = ''
            for i in key:
                str_key += str(key[i]) + chr(97+i)
            if str_key not in counter:
                counter[str_key] = []
            counter[str_key].append(s)

        ret = []
        for vals in counter.values():
            if len(vals) > 1:
                ret.extend(vals)
        return ret

       
if __name__ == "__main__":
    s = Solution()

    print s.anagrams(['eat', 'tea', 'and']) 
