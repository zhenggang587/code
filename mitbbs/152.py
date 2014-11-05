
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getSolution(self, head, n):
        fast = head
        i = 0
        while i < n:
            fast = fast.next
            i += 1

        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        

if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution()
