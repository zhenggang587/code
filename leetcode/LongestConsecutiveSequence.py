
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if not num:
            return 0

        num_set = set(num)
        has_visited = set()

        max_len = 1
        for n in num:
            if n in has_visited:
                continue
            has_visited.add(n)
            left = n - 1
            left_cnt = 0
            while left in num_set:
                left_cnt += 1
                has_visited.add(left)
                left -= 1
            right = n + 1
            right_cnt = 0
            while right in num_set:
                right_cnt += 1
                has_visited.add(right)
                right += 1
            if max_len < left_cnt + right_cnt + 1:
                max_len = left_cnt + right_cnt + 1

        return max_len



if __name__ == "__main__":
    s = Solution()

    print s.longestConsecutive([100])
