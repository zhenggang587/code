
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num_map = {}
        for i in range(len(num)):
            num_map[num[i]] = i

        for i in range(len(num)):
            sub = target - num[i]
            if sub in num_map and i != num_map[sub]:
                return (i + 1, num_map[sub] + 1)
        
if __name__ == "__main__":
    s = Solution()

    assert s.twoSum([2, 2, 11, 2], 4) == (1, 4)
    assert s.twoSum([3,2,4], 6) == (2, 3)
