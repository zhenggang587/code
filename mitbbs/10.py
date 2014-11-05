class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.conflict = False


class Solution:
    def getSolution(self, events):
        if not events:
            return

        events = sorted(events, key=lambda x : x.start)

        start, end = events[0].start, events[0].end
        j = 0
        i = 1
        while i < len(events):
            if events[i].start > end:
                j = i
                start, end = events[j].start, events[j].end
            else:
                events[j].conflict = events[i].conflict = True
                if events[i].end > end:
                    end = events[i].end
            i += 1
        

if __name__ == "__main__":
    s = Solution()
    
    events = [Event(1, 4), Event(5, 7), Event(5, 9), Event(10, 10)]
    s.getSolution(events)
    for e in events:
        print e.conflict
