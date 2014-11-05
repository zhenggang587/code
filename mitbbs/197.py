
class Solution:
    def decimal(self, n, d):
        if d == 0:
            return 0
        sign = 1
        if n < 0:
            n = -n
            sign = -sign
        if d < 0:
            d = -d
            sign = -sign

        real = n / d
        remain = n % d
        remains = {}
        decimals = []
        i = 0
        while remain:
            if remain not in remains:
                remains[remain] = i
            else:
                decimals.insert(remains[remain], '(')
                break
            remain *= 10
            digit, remain = divmod(remain, d)
            decimals.append(str(digit))
            i += 1
        if not remain:
            decimals.append('(0)')
        else:
            decimals.append(')')
        ret = str(real) + '.' + ''.join(decimals)
        if sign == -1:
            return '-' + ret
        return ret


            


if __name__ == "__main__":
    s = Solution()

    print s.decimal(1, 3)
    print s.decimal(2, 4)
    print s.decimal(22, -7)
