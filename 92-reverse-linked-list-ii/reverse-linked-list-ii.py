# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        m = ListNode(0,head)
        a = m
        t = 1
        while left > t:
            a = a.next
            t = t + 1
        cur = a.next
        prev = None
        k = 0
        while k < right - left + 1:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            k = k + 1
        t = a.next
        a.next = prev
        t.next = cur
        return m.next