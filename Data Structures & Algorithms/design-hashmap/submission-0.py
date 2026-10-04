class ListNode:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    size = 1000
    def __init__(self):
        self.hm = [ListNode() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        node = self.hm[self.hash(key)]
        found = False
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        node = self.hm[self.hash(key)]
        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next
        return -1
        

    def remove(self, key: int) -> None:
        node = self.hm[self.hash(key)]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def hash(self, key) -> int:
        return (key * 31) % self.size

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)