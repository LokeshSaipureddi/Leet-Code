class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        b = head
        while b :
            temp = b.next
            b.next = a
            a = b
            b = temp 
        return a