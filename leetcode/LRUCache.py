
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.data = {}
        self.pos_map = {}
        self.pos_list = []
        self.min_index = -1
        self.index = 0
        self.cap = capacity

    def addHits(self, key):
        self.pos_map[key] = self.index
        self.pos_list.append(key)

        self.index += 1


    def evict(self):
        while True:
            self.min_index += 1
            key = self.pos_list[self.min_index]
            if self.min_index == self.pos_map[key]:
                del self.pos_map[key]
                del self.data[key]
                return
        

    # @return an integer
    def get(self, key):
        if key not in self.data:
            return -1
        self.addHits(key)

        return self.data[key]
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.cap <= 0:
            return 
        if len(self.data) == self.cap and key not in self.data:
            self.evict()
        
        self.addHits(key)
        self.data[key] = value



if __name__ == "__main__":
    l = LRUCache(2)
    l.get(2)
    l.set(2, 6)
    l.get(1)
    l.set(1, 5)
    l.set(1, 2)
    l.get(1)
    print l.get(2)
