
class Solution:
    def getSolution(self, A):
        m = {}
        for num in A:
            index = 0
            while True:
                if index not in m:
                    m[index] = {}
                d = num % 10
                if d not in m[index]:
                    m[index][d] = 0
                m[index][d] += 1

                index += 1
                num /= 10
                if not num:
                    break

        ret = 0
        for index, val in m.items():
            digits = val.values()
            for i in range(len(digits)):
                for j in range(i + 1, len(digits)):
                    ret += digits[i] * digits[j]
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([2173896, 2233796])
