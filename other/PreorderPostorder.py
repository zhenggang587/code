
class Solution:
    def getSolution(self, preorder, postorder):
        preorder = preorder[1:]
        postorder = postorder[:-1]
        if not preorder:
            return 1

        index = postorder.index(preorder[0])
        if index == len(postorder) - 1:
            return 2 * self.getSolution(preorder, postorder)
        else:
            return self.getSolution(preorder[:index+1], postorder[:index+1]) * self.getSolution(preorder[index+1:], postorder[index+1:])



if __name__ == "__main__":
    s = Solution()

    print s.getSolution([1, 2, 3], [2, 3, 1])

