
class BigNum:
    def __init__(self, s):
        self.arr = []
        for i in range(len(s) - 1, -1, -1):
            self.arr.append(int(s[i]))

    def add(self, num):
        val = num
        for i in range(len(self.arr)):
            self.arr[i] += val
            if self.arr[i] >= 10:
                val = self.arr[i] / 10
                self.arr[i] %= 10
            else:
                break
        if val:
            self.arr.append(val)

    def __str__(self):
        ret = ''
        for i in range(len(self.arr) - 1, -1, -1):
            ret += str(self.arr[i])
        return ret
        

if __name__ == "__main__":
    b = BigNum('999999999999')
    b.add(2)
    
    print b
