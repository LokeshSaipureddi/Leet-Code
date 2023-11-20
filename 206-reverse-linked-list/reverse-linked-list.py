class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        p=None
        while a:
            t=a.next
            a.next=p
            p=a
            a=t
        return p    
