
class Solution:
    def getSolution(self, dict):
        s = set(dict)
        into = {}
        out = {}
        for w in s:
            out[w] = []

        for w in s:
            into[w] = 0
            for i in range(len(w)):
                sw = w[:i] + w[i+1:]
                if sw in s:
                    into[w] += 1
                    out[sw].append(w)

        ready = []
        counter = {}
        ret = 0
        for w, e in into.items():
            counter[w] = 0
            if e == 0:
                ready.append(w)
                counter[w] = 1
                ret = 1

        while ready:
            w = ready.pop(0)
            for n in out[w]:
                into[n] -= 1
                if into[n] == 0:
                    ready.append(n)
                tmp = counter[w] + 1
                if tmp > counter[n]:
                    counter[n] = tmp
                if tmp > ret:
                    ret = tmp
        return ret


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution(['a', 'at', 'cat', 'chat', 'chart', 'as', 'sas', 'saas', 'ssaat', 'ssaas', 'ssaast'])
