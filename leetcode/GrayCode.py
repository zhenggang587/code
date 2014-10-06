
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if not n:
            return [0]
        
        ret = []
        bits = ''
        for i in range(n):
            bits += '0'
        has_visited = set()
        self.traverse(bits, has_visited, ret)
        return ret

    def traverse(self, bits, has_visited, ret):
        if bits in has_visited:
            return

        has_visited.add(bits)
        ret.append(self.bin2dec(bits))
        for i in range(len(bits) - 1, -1, -1):
            c = '0' if bits[i] == '1' else '1'
            temp = bits[:i] + c + bits[i+1:]
            self.traverse(temp, has_visited, ret)

    def bin2dec(self, bits):
        ret = 0
        for b in bits:
            ret = ret * 2 + int(b)
        return ret
        
       
if __name__ == "__main__":
    s = Solution()

    print s.grayCode(1)
