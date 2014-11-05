
# B cann't have duplicate num

class Solution:
    def getSolution(self, A, B):
        if not B:
            return []

        m = {}
        for i in range(len(A)):
            num = A[i]
            if num in B:
                if num not in m:
                    m[num] = []
                m[num].append(i)

        p = [0 for i in range(len(B))]
        if B[0] not in m:
            return []

        minRange = (1 << 31)
        minStart = minEnd = 0

        findex = 0
        while findex < len(m[B[0]]):
            p[0] = m[B[0]][findex]
            for i in range(1, len(B)):
                num = B[i]
                if num not in m:
                    return []
                index = 0
                while index < len(m[num]) and m[num][index] <= p[i - 1]:
                    index += 1
                if index == len(m[num]):
                    return []
                p[i] = m[num][index]
            if p[len(B) - 1] - p[0] < minRange:
                minRange = p[len(B) - 1] - p[0]
                minStart = p[0]
                minEnd = p[len(B) - 1]
            findex += 1

        return A[minStart:minEnd + 1]



if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([1, 9, 3, 4, 12, 13, 9, 12, 21], [9, 9])
