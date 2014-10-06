
class TreeNode:
    def __init__(self):
        self.next = [None for i in range(26)]
        self.fail = None
        self.val = None

class Solution:
    def getSolution(self, s, words):
        root = self.buildTree(words)

        index = 0
        p = root
        maxLen = 0
        ret = ''
        while index < len(s):
            i = ord(s[index]) - ord('a')
            while not p.next[i] and p != root:
                p = p.fail
            p = p.next[i]
            if not p:
                p = root
            temp = p
            while temp != root and temp.val:
                if len(temp.val) > maxLen:
                    maxLen = len(temp.val)
                    ret = temp.val
                temp = temp.fail
            index += 1
        return ret

    def buildTree(self, words):
        root = TreeNode()

        for word in words:
            cur = root
            for c in word:
                i = ord(c) - ord('a')
                if not cur.next[i]:
                    cur.next[i] = TreeNode()
                cur = cur.next[i]
            cur.val = word

        queue = [root]
        while queue:
            temp = queue.pop(0)
            for i in range(26):
                if not temp.next[i]:
                    continue
                if temp == root:
                    temp.next[i].fail = root
                else:
                    p = temp.fail
                    while p:
                        if p.next[i]:
                            temp.next[i].fail = p.next[i]
                            break
                        p = p.fail
                    if not p:
                        temp.next[i].fail = root
                queue.append(temp.next[i])
        return root

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution('sherooo', ['say', 'she', 'shr', 'hero'])
