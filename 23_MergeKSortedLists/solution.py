# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        d = {}

        for l in lists:
            while l is not None:
                if l.val not in d:
                    d[l.val] = 0
                d[l.val] += 1

                l = l.next

        head = None
        curr = head

        for key in sorted(d.keys()):
            while d[key] > 0:
                if head is None:
                    head = ListNode(key)
                    curr = head
                else:
                   curr.next = ListNode(key)
                   curr = curr.next

                d[key] -= 1

        return head
