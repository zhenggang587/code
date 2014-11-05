
class Solution:
    def getSolution(self, A):
        m = {0: [-1]}
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            if sum not in m:
                m[sum] = []
            m[sum].append(i)

        ret = []
        for pairs in m.values():
            if len(pairs) <= 1:
                continue
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    ret.append((pairs[i] + 1, pairs[j]))
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([0, -1, 1])
