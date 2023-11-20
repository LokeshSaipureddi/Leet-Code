# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s,f=head,head
        while f and f.next:
            s=s.next
            f=f.next.next  
        p=None
        while s:
            t=s.next
            s.next=p
            p=s
            s=t
        b=head    
        while p:
            if b.val!=p.val:
                return False
            b=b.next
            p=p.next
        return True                   