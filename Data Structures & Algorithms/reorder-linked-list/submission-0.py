# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        copy = []
        while head:
            copy.append(head)
            head = head.next
        
        l, r = 0, len(copy) - 1

        while l < r:
            copy[l].next = copy[r]
            l += 1
            if l >= r:
                break
            copy[r].next = copy[l]
            r -= 1
        copy[l].next = None