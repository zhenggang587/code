
class Entry:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None

class HashMap:
    def __init__(self):
        self.table = [None for i in range(1)]
        self.elemCnt = 0
        self.loadFactor = 0.75

    def doPut(self, table, k, v, flag):
        idx = k & (len(table) - 1)
        if not table[idx]:
            table[idx] = Entry(k, v)
            if flag:
                self.elemCnt += 1
        else:
            entry = table[idx]
            flag = False
            while True:
                if entry.k == k:
                    entry.v = v
                    flag = True
                    break
                if not entry.next:
                    break
                entry = entry.next
            if not flag:
                entry.next = Entry(k, v)
                if flag:
                    self.elemCnt += 1

    def put(self, k, v):
        if self.elemCnt > len(self.table) * self.loadFactor:
            self.resize()
        self.doPut(self.table, k, v, True)

    def resize(self):
        newtable = [None for i in range(2 * len(self.table))]
        for i in range(len(self.table)):
            entry = self.table[i]
            while entry:
                self.doPut(newtable, entry.k, entry.v, False)
                entry = entry.next
        self.table = newtable
        
    def get(self, k):
        idx = k & (len(self.table) - 1)
        if not self.table[idx]:
            return None
        else:
            entry = self.table[idx]
            while entry:
                if entry.k == k:
                    return entry.v
                entry = entry.next
            return None
        
if __name__ == "__main__":
    h = HashMap()

    h.put(1, 10)
    print h.get(2)
    print h.get(1)
    h.put(1, 5)
    h.put(2, 3)
    print h.get(2)
    print h.get(1)
    h.put(3, 3)

