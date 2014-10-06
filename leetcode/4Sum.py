import time

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        ret = []
        num.sort()
        n = len(num)
        for i in range(n - 3):
            if i != 0 and num[i] == num[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j != i + 1 and num[j] == num[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sum = num[i] + num[j] + num[left] + num[right]
                    if sum == target:
                        ret.append((num[i], num[j], num[left], num[right]))
                        left += 1
                        right -= 1

                        while left < right and num[left] == num[left - 1]:
                            left += 1
                        while right > left and num[right] == num[right + 1]:
                            right -= 1
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1

        return [list(x) for x in set(ret)]
        
if __name__ == "__main__":
    s = Solution()

    time1 = time.time()
    print s.fourSum([1, 0, -1, 0, -2, 2], 0)
    print s.fourSum([-500,-490,-471,-456,-422,-412,-406,-398,-381,-361,-341,-332,-292,-288,-272,-236,-235,-227,-207,-203,-185,-119,-59,-13,4,5,46,72,82,91,92,130,130,140,145,159,187,207,211,226,239,260,262,282,290,352,377,378,386,405,409,430,445,478,481,498], -3213
    )
    print time.time() - time1
