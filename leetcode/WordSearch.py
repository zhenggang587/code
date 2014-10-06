
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
        if board[i][j] != word[index]:
            return False
        if index == len(word) - 1:
            return True

        has_visited.add((i, j))
        if i > 0 and (i - 1, j) not in has_visited:
            if self.traverse(board, i - 1, j, word, index + 1, has_visited):
                return True
        if j > 0 and (i, j - 1) not in has_visited:
            if self.traverse(board, i, j - 1, word, index + 1, has_visited):
                return True
        if i < len(board) - 1 and (i + 1, j) not in has_visited:
            if self.traverse(board, i + 1, j, word, index + 1, has_visited):
                return True
        if j < len(board[0]) - 1 and (i, j + 1) not in has_visited:
            if self.traverse(board, i, j + 1, word, index + 1, has_visited):
                return True

        has_visited.remove((i, j))
        return False
            

        
if __name__ == "__main__":
    s = Solution()

    
    print s.exist(["aa"], "aa")
    print s.exist([
    "ABCE",
    "SFCS",
    "ADEE"
    ], "ABCCED")
