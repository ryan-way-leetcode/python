# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, head):
        if head is None:
            return False

        return self.val == head.val and self.next == head.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        c = n = head
        while c is not None:
            n, c.next = c.next, p
            p, c = c, n
        return p