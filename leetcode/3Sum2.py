import time

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        ret = []
        num.sort()
        n = len(num)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                tmp = num[i] + num[j] + num[k]
                if tmp < 0:
                    j += 1
                elif tmp > 0:
                    k -= 1
                else:
                    ret.append((num[i], num[j], num[k]))

                    j += 1
                    k -= 1
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    while j < k and num[k] == num[k + 1]:
                        k -= 1
                
        return [list(x) for x in set(ret)]
        
if __name__ == "__main__":
    s = Solution()

    print s.threeSum([-1, 0, 1, 2, -1, -4])
    time1 = time.time()
    print s.threeSum([-7,2,1,10,9,-10,-5,4,13,-9,-4,6,11,-12,-6,-9,-6,-9,-11,-4,10,10,-3,-1,-4,-7,-12,-15,11,5,14,11,-7,-8,6,9,-2,9,-10,-12,-15,2,10,4,5,11,10,6,-13,6,-13,12,-7,-9,-12,4,-9,13,-4,10,4,-12,6,4,-5,-10,-2,0,14,4,4,6,13,-9,-5,-5,-13,12,-14,11,3,10,8,11,-13,4,-8,-7,2,4,10,13,7,2,2,9,-1,8,-5,-10,-3,6,3,-5,12,6,-3,6,3,-2,2,14,-7,-13,10,-13,-2,-12,-4,8,-1,13,6,-9,0,-14,-15,6,9]
    )
    print time.time() - time1
