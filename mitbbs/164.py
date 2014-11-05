
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def encode(self, head):
        ret = ''
        cur = head
        while cur:
            ret += str(len(cur.val)) + '#' + cur.val
            cur = cur.next
        return ret

    def decode(self, s):
        start = end = 0
        p = dummy = ListNode(0)
        while end < len(s):
            if s[end] != '#':
                end += 1
            else:
                l = int(s[start:end])
                start = end + 1
                p.next = ListNode(s[start:start+l])
                p = p.next
                start = end = start + l
        return dummy.next
        
    def printList(self, list):
        cur = list
        while cur:
            print cur.val
            cur = cur.next

if __name__ == "__main__":
    s = Solution()
    
    node1 = ListNode('156')
    node2 = ListNode('')
    node3 = ListNode('aaaaaaa')
    node1.next = node2
    node2.next = node3
    s.printList(s.decode(s.encode(node1)))
