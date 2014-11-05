
# follow up: k unique char
class Solution:
    def getSolution(self, s):
        if len(s) <= 2:
            return s

        fstart = fend = 0
        sstart = send = -1
        maxStart = maxEnd = 0
        for i in range(1, len(s)):
            if s[i] == s[fend]:
                fend = i
            elif sstart == -1:
                sstart = send = i
            elif s[i] == s[send]:
                send = i
            else:
                end = max(fend, send)
                start = min(fstart, sstart)
                if end - start > maxEnd - maxStart:
                    maxEnd = end
                    maxStart = start
                fstart = min(fend, send) + 1
                fend = i - 1
                sstart = send = i

        end = max(fend, send)
        start = min(fstart, sstart)
        if end - start > maxEnd - maxStart:
            maxEnd = end
            maxStart = start
        return s[maxStart:maxEnd + 1]
                
            


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution("aabaadddddaa")
