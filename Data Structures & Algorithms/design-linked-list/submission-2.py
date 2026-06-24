class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.dummy = ListNode(-1)


    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):
            if not cur:
                return -1
            cur = cur.next
        return cur.val if cur else -1
        

    def addAtHead(self, val: int) -> None:
        # first node
        if not self.head:
            self.head = self.tail = ListNode(val)
            self.dummy.next = self.head
            return

        tmp = ListNode(val, self.head)
        self.head = tmp
        self.dummy.next = self.head

    def addAtTail(self, val: int) -> None:

        #first node
        if not self.tail:
            self.head = self.tail = ListNode(val)
            self.dummy.next = self.head
            return

        tmp = ListNode(val)
        self.tail.next = tmp
        self.tail = tmp
        self.dummy.next = self.head
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        prev = self.dummy
        for i in range(index):
            if not prev:
                return
            prev = prev.next

        tmp = ListNode(val, prev.next)
        prev.next = tmp
        if prev == self.tail:
            self.tail = tmp



    def deleteAtIndex(self, index: int) -> None:
        prev = self.dummy
        for _ in range(index):
            if not prev.next:
                return
            prev = prev.next
        
        if not prev.next:
            return
        if prev.next == self.tail:
            self.tail = prev if prev != self.dummy else None
        prev.next = prev.next.next
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)