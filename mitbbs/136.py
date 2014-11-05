
class Solution:
    def getSolution(self, A):
        m = {}
        for a in A:
            key = ''.join(sorted(a))
            if key not in m:
                m[key] = []
            m[key].append(a)

        ret = []
        for key, list in m.items():
            ret.append(list)
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(['abc', 'def', 'xyz', 'fde', 'fed', 'cab'])
