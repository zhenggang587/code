
# see 11.py

class Solution:
    def getSolution(self, A):
        indegree = {}
        out = {}

        n = len(A)
        for i in range(n - 1):
            a = A[i]
            b = A[i + 1]
            j = 0
            while j < len(a) and j < len(b):
                if a[j] != b[j]:
                    c1, c2 = a[j], b[j]
                    if c1 not in out:
                        out[c1] = []
                    if c2 not in out:
                        out[c2] = []
                    out[c1].append(c2)

                    if c1 not in indegree:
                        indegree[c1] = 0
                    if c2 not in indegree:
                        indegree[c2] = 0
                    indegree[c2] += 1
                    break
                j += 1

        ready = [c for c, cnt in indegree.items() if cnt == 0]
        seq = []
        while ready:
            c = ready.pop(0)
            seq.append(c)
            for o in out[c]:
                indegree[o] -= 1
                if indegree[o] == 0:
                    ready.append(o)
        return seq
                    

         

if __name__ == "__main__":
    s = Solution()

    print s.getSolution(['bc', 'ba', 'cba'])
