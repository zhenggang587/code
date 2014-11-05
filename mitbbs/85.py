
class Person:
    def __init__(self, x):
        self.val = x
        self.father = None
        self.mother = None

class Solution:
    def __init__(self, persons):
        self.persons = persons
        self.arr = {}
        for p in self.persons:
            root = []
            self.traverse(p, root)
            self.arr[p.val] = root

    def traverse(self, p, root):
        if not p:
            return
        if not p.father and not p.mother:
            root.append(p.val)
            return

        self.traverse(p.father, root)
        self.traverse(p.mother, root)
                
    def find(self, p, q):
        if list(set(self.arr[p.val]) & set(self.arr[q.val])):
            return True
        return False
        

if __name__ == "__main__":
    
    p1 = Person(1)
    p2 = Person(2)
    p3 = Person(3)
    p3.father = p1
    p3.mother = p2

    s = Solution([p1, p2, p3])
        
    print s.find(p1, p2)
