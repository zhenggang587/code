
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if not gas:
            return -1

        min_left = (1 << 31) - 1
        min_index = -1
        left = 0
        for i in range(len(gas)):
            left += gas[i] - cost[i]
            if left < min_left:
                min_left = left
                min_index = i
        if left < 0:
            return -1
        else:
            return (min_index + 1) % len(gas)

        
if __name__ == "__main__":
    s = Solution()

    print s.canCompleteCircuit([0, 2], [0, 2])
