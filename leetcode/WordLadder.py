import string

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        queue = [start]
        has_visited = set(start)

        level = 1
        while queue:
            cnt = len(queue)
            for k in range(cnt):
                cur = queue.pop(0)
                if cur == end:
                    return level

                for i in range(len(cur)):
                    for c in string.lowercase:
                        word = cur[:i] + c + cur[i+1:]
                        if word == end:
                            return level + 1
                        if word in dict and word not in has_visited:
                            queue.append(word)
                            has_visited.add(word)
            level += 1

        return 0


if __name__ == "__main__":
    s = Solution()
    
    print s.ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
