
class Solution:
    def getSolution(self, s1, s2):
        bucket = [0 for c in s2]

        remain = []
        for c in s1:
            if c in s2:
                bucket[s2.index(c)] += 1
            else:
                remain.append(c)

        prefix = ''
        for i in range(len(bucket)):
            if bucket[i] > 0:
                prefix += bucket[i] * s2[i]

        if not remain:
            return [prefix]

        perm = [[remain[0]]]
        for i in range(1, len(remain)):
            new = []
            for p in perm:
                for j in range(i + 1):
                    new.append(p[:j] + [remain[i]] + p[j:])
            perm = new

        ret = []
        for s in perm:
            ret.append(prefix + ''.join(s))

        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('house', 'soup')
