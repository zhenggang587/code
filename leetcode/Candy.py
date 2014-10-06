
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings:
            return 0

        left = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        right = [1 for i in range(len(ratings))]
        ret = left[len(left) - 1] if left[len(left) - 1] > 1 else 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            ret += left[i] if left[i] > right[i] else right[i]

        return ret
        

if __name__ == "__main__":
    s = Solution()

    print s.candy([1, 1, 5, 4, 3])
