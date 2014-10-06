
class Queue:
    def __init__(self):
        self.data = []
        self.minq = []

    def insert(self, val):
        self.data.append(val)
        if not self.minq:
            self.minq.append(val)
        else:
            index = 0
            while index < len(self.minq):
                if self.minq[index] > val:
                    break
                index += 1
            self.minq = self.minq[:index]
            self.minq.append(val)


    def delete(self):
        if len(self.data) <= 0:
            raise Exception('test')

        val = self.data.pop(0)
        if val == self.min():
            self.minq.pop(0)
        return val

    def min(self):
        if not self.minq:
            raise Exception('test')

        return self.minq[0] 


if __name__ == "__main__":
    q = Queue()
    
    q.insert(3)
    print q.min()
    q.insert(1)
    q.insert(1)
    print q.min()
    print q.delete()
    print q.delete()
