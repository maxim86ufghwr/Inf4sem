class Box:
    def __init__(self, el=None):
        self.el = el
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def contains(self, el):
        lastbox = self.head
        while lastbox:
            if el == lastbox.el:
                return True
            else:
                lastbox = lastbox.next
        return False

    def addToEnd(self, new):
        newbox = Box(new)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while lastbox.next:
            lastbox = lastbox.next
        newbox.prev = lastbox
        lastbox.next = newbox
    def get(self, Index):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= Index:
            if boxIndex == Index:
                return lastbox.el
            boxIndex = boxIndex + 1
            lastbox = lastbox.next
    def removeBox(self, rmel):
        head = self.head
        if head is not None:
            if head.el == self.get(rmel):
                self.head = head.next
                head = None
                return
        while head is not None:
            if head.el == self.get(rmel):
                break
            last = head
            head = head.next
        if head == None:
            return
        last.next = head.next
        head = None
    def __len__(self):
        lastbox = self.head
        l = 0
        while lastbox:
            lastbox = lastbox.next
            l+=1
        return l
    def print_l(self):
        lastbox = self.head
        a = []
        while lastbox:
            a.append(lastbox.el)
            lastbox = lastbox.next
        print(a)
        return
    def addSomeWhere(self, new, index):
        newbox = Box(new)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        if index == 0:
            lastbox.prev = newbox
            newbox.next = lastbox
            return
        c = 0
        while c < index-1:
            lastbox = lastbox.next
            c+=1
        if lastbox.next:
            newbox.prev = lastbox
            re = lastbox.next
            lastbox.next = newbox
            newbox.next = re
            return
a = LinkedList()
a.addSomeWhere(4, 0)
a.addToEnd(1)
a.addToEnd(2)
a.addToEnd(3)
print(len(a))
a.print_l()
print(a.get(0))
a.addSomeWhere(5, 3)
a.print_l()
a.removeBox(0)
a.print_l()
