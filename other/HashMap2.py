
class Entry:
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __str__(self):
        return str(self.k) + ":" + str(self.v)

class HashMap:
    def __init__(self):
        self.table = [None for i in range(4)]
        self.elemCnt = 0
        self.loadFactor = 0.75

    def doPut(self, table, k, v):
        idx = k & (len(table) - 1)
        if not table[idx]:
            table[idx] = Entry(k, v)
            self.elemCnt += 1
        else:
            cur = idx
            while True:
                if cur < 0:
                    cur = len(table) - 1
                entry = table[cur]
                if not entry:
                    table[cur] = Entry(k, v)
                    self.elemCnt += 1
                    break
                if entry.k == k:
                    entry.v = v
                    break
                cur = cur - 1

    def put(self, k, v):
        if self.elemCnt > len(self.table) * self.loadFactor:
            self.resize()
        self.doPut(self.table, k, v)

    def resize(self):
        newtable = [None for i in range(2 * len(self.table))]
        for i in range(len(self.table)):
            entry = self.table[i]
            self.doPut(newtable, entry.k, entry.v)
        self.table = newtable
        
    def get(self, k):
        idx = k & (len(self.table) - 1)
        if not self.table[idx]:
            return None
        else:
            entry = self.table[idx]
            cur = idx
            while True:
                if cur < 0:
                    cur = len(self.table) - 1
                entry = self.table[cur]
                if not entry:
                    return None
                if entry.k == k:
                    return entry.v
                cur = cur - 1
            return None
        
if __name__ == "__main__":
    h = HashMap()

    h.put(1, 10)
    h.put(5, 1)
    print h.get(1)
    print h.get(5)

