
class Solution:
    def getSolution(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        q = [0 for i in range(n + 1)]
        path = [0 for i in range(n + 1)]
        if nums[1] == nums[0]:
            q[2] = 2 * 2
        for i in range(2, n):
            q[i + 1] = q[i - 2]
            path[i + 1] = i - 2
            if q[i - 1] > q[i + 1]:
                path[i + 1] = i - 1

            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                if q[i - 2] + 2 * 3 > q[i + 1]:
                    q[i + 1] = q[i - 2] + 2 * 3
                    path[i + 1] = i - 2
            elif self.isGood(nums[i-2:i + 1]):
                if q[i - 2] + 3 > q[i + 1]:
                    q[i + 1] = q[i - 2] + 3
                    path[i + 1] = i - 2
            if nums[i] == nums[i - 1]:
                if q[i - 1] + 2 * 2 > q[i + 1]:
                    q[i + 1] = q[i - 1] + 2 * 2
                    path[i + 1] = i - 1

        p = n 
        ret = []
        while p:
            ret.append(nums[path[p]:p])
            p = path[p]
        return ret[::-1]

    def isGood(self, l):
        m = {}
        for i in l:
            if i not in m:
                m[i] = 0

        return len(m) == 2


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('0000166')
