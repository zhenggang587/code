
class Solution:
    def getSolution(self, A, B, pa, pb):
        map_a = {}
        m = len(A)
        n = len(B)
        for i in range(m):
            val = A[i][pa]
            if val not in map_a:
                map_a[val] = []
            map_a[val].append(A[i])

        map_b = {}
        for j in range(n):
            val = B[j][pb]
            if val not in map_b:
                map_b[val] = []
            map_b[val].append(B[j])

        ret = []
        for val, rows in map_a.items():
            if val not in map_b:
                for row in rows:
                    ret.append(row + ['-'] * (n - 1))
            else:
                for rowa in rows:
                    for rowb in map_b[val]:
                        del rowb[pb]
                        ret.append(rowa + rowb)

        for val, rows in map_b.items():
            if val not in map_a:
                for row in rows:
                    ret.append(['-'] * (m - 1) + row)
        return ret

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 2], [2, 5]], [[3, 4], [2, 8]], 1, 0)
