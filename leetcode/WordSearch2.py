
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    has_visited = set()
                    if self.traverse(board, i, j, word, 0, has_visited):
                        return True

        return False

    def traverse(self, board, i, j, word, index, has_visited):
        if index == len(word):
            return True
        if (i, j) in has_visited:
            return False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != word[index]:
            return False

        has_visited.add((i, j))
        ret = self.traverse(board, i - 1, j, word, index + 1, has_visited) \
                or self.traverse(board, i, j - 1, word, index + 1, has_visited) \
                or self.traverse(board, i + 1, j, word, index + 1, has_visited) \
                or self.traverse(board, i, j + 1, word, index + 1, has_visited)

        has_visited.remove((i, j))
        return ret
            

        
if __name__ == "__main__":
    s = Solution()

    
    print s.exist(["aa"], "aa")
    print s.exist([
    "ABCE",
    "SFCS",
    "ADEE"
    ], "ABCCED")
