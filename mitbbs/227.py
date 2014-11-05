
# 还可以变成14 * 4的矩阵
class Solution:
    def getSolution(self, cards):
        cards = sorted(cards)
        sameColor = []
        self.traverseSameColor(cards, 0, [], sameColor)
        shunzi = self.traverseShunzi(cards)
        ret = []
        for sub in sameColor:
            if sub in shunzi:
                ret.append(sub)
        return ret

    def traverseShunzi(self, cards):
        cardMap = {}
        for card in cards:
            if card[0] not in cardMap:
                cardMap[card[0]] = []
            cardMap[card[0]].append(card[1])

        hasVisited = set()
        paths = []
        for i in range(len(cards)):
            num = cards[i][0]
            path = []
            if num in hasVisited:
                continue

            hasVisited.add(num)
            path.append((num, cardMap[num]))
            k = num - 1
            while k > 0 and k in cardMap:
                hasVisited.add(k)
                path.insert(0, (k, cardMap[k]))
                k -= 1
            k = num + 1
            while k <= 13 and k in cardMap:
                hasVisited.add(k)
                path.append((k, cardMap[k]))
                k += 1
            if len(path) >= 5:
                for index in range(len(path) - 5 + 1):
                    self._traverseShunzi(path, index, [], paths)
        return paths

    def _traverseShunzi(self, d, index, path, paths):
        if len(path) == 5:
            paths.append(path[:])
            return
        if index >= len(d):
            return

        num = d[index][0]
        for color in d[index][1]:
            path.append([num, color])
            self._traverseShunzi(d, index + 1, path, paths)
            path.pop()
    
    def traverseSameColor(self, cards, index, path, paths):
        if len(path) == 5:
            paths.append(path[:])
            return

        for k in range(index, len(cards)):
            if not path or cards[k][1] == path[0][1]:
                path.append(cards[k])
                self.traverseSameColor(cards, k + 1, path, paths)
                path.pop()


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[2, 0], [1, 0], [3, 0], [4, 0], [5, 0], [6, 1], [7, 0]])
